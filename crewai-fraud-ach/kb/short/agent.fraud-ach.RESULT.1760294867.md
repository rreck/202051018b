```json
{
  "id": "ad5379f8f49f6ec2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294867,
  "host_pid": "9e6742732c60:1",
  "hash": "8dcf94e9724c5371cff27b77dc3e11336be73c2cf77382cf65a585d6bbdde6b8",
  "cid": "QmV18dcf94e9724c5371cff27b77dc3e11336be73c2c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294867,
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
      "evaluated_at": 1760294868
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
  "sig": "bc5f2060485f2fbf085429db560e51be227b3eba46153899803e2a799c750da5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246132965
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 108163986, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285763, 'matching_hash': 'ed6ec2b6e100ea2c'}}}