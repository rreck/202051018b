```json
{
  "id": "07384e6629b106a0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287576,
  "host_pid": "9e6742732c60:1",
  "hash": "ed27e2db530be1e05047032a49cd3eb026c1344d24771d1525d0bdc3eb3ce8c3",
  "cid": "QmV1ed27e2db530be1e05047032a49cd3eb026c1344d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287576,
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
      "evaluated_at": 1760287576
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
  "sig": "99f2f55e78fba82937ef7f856c4a5d7bb275e84f9c409f5721cfbd0bacb29fff"
}
```

Fraud detected: duplicate_transaction (score: 82)
Transaction: 044000030478037
Details: {'velocity': {'fraud_detected': True, 'risk_score': 80, 'details': {'transaction_count': 65, 'threshold': 50, 'total_amount': 14017900, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 64, 'first_seen': 1760285763, 'matching_hash': 'a92b61c306bd8c34'}}}