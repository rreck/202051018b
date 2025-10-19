```json
{
  "id": "0782956cbdc0e41d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292687,
  "host_pid": "9e6742732c60:1",
  "hash": "4b36a61d1e49bc97422626f9bc695df052c4619481707ddc43a934dc61bb4899",
  "cid": "QmV14b36a61d1e49bc97422626f9bc695df052c46194",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292687,
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
      "evaluated_at": 1760292687
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
  "sig": "602f95bd1f130a49462d318b6d47d83bc5254e42abe1b679b2362f5e722094ec"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039250274
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 23043545, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285763, 'matching_hash': 'd24fc6d094fa29d9'}}}