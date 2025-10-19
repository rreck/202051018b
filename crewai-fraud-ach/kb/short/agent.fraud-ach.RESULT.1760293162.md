```json
{
  "id": "d3072b23588ad8a1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293162,
  "host_pid": "9e6742732c60:1",
  "hash": "a64edcc0dbaf1c1d5a1155946350200bd4dc888c274b72e27955b44554b6aa8a",
  "cid": "QmV1a64edcc0dbaf1c1d5a1155946350200bd4dc888c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293162,
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
      "evaluated_at": 1760293162
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
  "sig": "766fe220bbdb4252c928c47c4a2e97b3936bdceb56c001e2231ad2c704a9c783"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276193597
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 54046620, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285763, 'matching_hash': 'c482c58c8f3e1991'}}}