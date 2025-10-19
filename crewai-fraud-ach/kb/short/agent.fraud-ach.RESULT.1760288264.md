```json
{
  "id": "b4abcd47662a3923",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288264,
  "host_pid": "9e6742732c60:1",
  "hash": "86a49e032a832343a9f5a36802794d4ad3d55719a0a90cb6c149cf9194efb791",
  "cid": "QmV186a49e032a832343a9f5a36802794d4ad3d55719",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288264,
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
      "evaluated_at": 1760288264
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
  "sig": "79ff83191ea9c2207764c053a652b63e86ba5a79d69a0ab788f92685fca13080"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464670752
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 88, 'threshold': 50, 'total_amount': 36742904, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 87, 'first_seen': 1760285763, 'matching_hash': '207898f44ec5d129'}}}