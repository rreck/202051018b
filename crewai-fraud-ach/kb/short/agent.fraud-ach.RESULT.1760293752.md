```json
{
  "id": "48b75540e6289fe4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293752,
  "host_pid": "9e6742732c60:1",
  "hash": "f9f5cbeb01900ed3c28cb3176d5011486fb5a15b141fcb6169658b8410e5e4f4",
  "cid": "QmV1f9f5cbeb01900ed3c28cb3176d5011486fb5a15b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293752,
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
      "evaluated_at": 1760293752
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
  "sig": "63a2edb4138712dd1ccdab1dfb7d631ab3dee8494db0ad241823a7fa36195962"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276193597
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 57091500, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285763, 'matching_hash': 'c482c58c8f3e1991'}}}