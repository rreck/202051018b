```json
{
  "id": "13aba763c6bab9c5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292775,
  "host_pid": "9e6742732c60:1",
  "hash": "e75dadf26902b7905ee89847c3d6ddd41385d28ca2c4cc57d64e6f7f2a140718",
  "cid": "QmV1e75dadf26902b7905ee89847c3d6ddd41385d28c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292775,
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
      "evaluated_at": 1760292775
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
  "sig": "1a9826849fde4f1141b2495d7d21b2b9709466d3b768f63e2aeb381a072a2ec2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037990803
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 47713750, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285763, 'matching_hash': 'be616144f18eac0b'}}}