```json
{
  "id": "54f8222467f235b2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288956,
  "host_pid": "9e6742732c60:1",
  "hash": "5c94436b09c6dc33560004b549fc6143e95ce81836824b6d059650ae1ca5d539",
  "cid": "QmV15c94436b09c6dc33560004b549fc6143e95ce818",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288956,
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
      "evaluated_at": 1760288956
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
  "sig": "460e777b6e22a64fd172d55316f16e12fc6da0da9153605e712a2e74f39f97f0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150096733
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 109, 'threshold': 50, 'total_amount': 14710640, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 108, 'first_seen': 1760285763, 'matching_hash': 'a29467afaa3320eb'}}}aly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5513113}}}