```json
{
  "id": "1e42a5ef3757dbaa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293231,
  "host_pid": "9e6742732c60:1",
  "hash": "19aa00b2124b7c1218317abc9956f447e3995825a7fa6a3ce3f815d2bbb3a620",
  "cid": "QmV119aa00b2124b7c1218317abc9956f447e3995825",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293231,
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
      "evaluated_at": 1760293231
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
  "sig": "e0334a96ecf32b83f5e0e4dcd74232dfe08762e700646d42d80dcc1852421e73"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026184073
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 66815294, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285763, 'matching_hash': '5c433365b4c36f89'}}}