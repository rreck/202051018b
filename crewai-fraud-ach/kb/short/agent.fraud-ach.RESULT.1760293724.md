```json
{
  "id": "5138f18dc0e76e64",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293724,
  "host_pid": "9e6742732c60:1",
  "hash": "4674161467efd9cb3b17392cc7eaa64adad0bf1f2cbbb0be8ce3dfd78852208d",
  "cid": "QmV14674161467efd9cb3b17392cc7eaa64adad0bf1f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293724,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760293724
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "823f7b94c99cab5206d72605f9ec4600796973d96752d126e69abf1b5dcbcffe"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461002751
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 75294464, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285763, 'matching_hash': 'a9820f16c3d139ec'}}}