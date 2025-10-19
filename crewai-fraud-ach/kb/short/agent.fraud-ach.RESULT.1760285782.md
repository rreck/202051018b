```json
{
  "id": "feba3337ad2ad139",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285782,
  "host_pid": "9e6742732c60:1",
  "hash": "05629374ffa2a78ca7153511e41240e14ca6f1285b99a5ecde083c11c1d33856",
  "cid": "QmV105629374ffa2a78ca7153511e41240e14ca6f128",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285782,
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
      "evaluated_at": 1760285782
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
  "sig": "4d94e5de894b768369e2d425aaf33d4c3526b5efd05cf2864c0ffd4d77627142"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032692891
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 78, 'threshold': 50, 'total_amount': 35456928, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 77, 'first_seen': 1760284979, 'matching_hash': '069830b10839223a'}}}'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7743228}}}