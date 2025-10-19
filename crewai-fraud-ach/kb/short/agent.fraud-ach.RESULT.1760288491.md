```json
{
  "id": "8823b311ef50c9de",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288491,
  "host_pid": "9e6742732c60:1",
  "hash": "a1a24df45b2d64fade922b12177c5995a3794861f684ff70b0740249351c111e",
  "cid": "QmV1a1a24df45b2d64fade922b12177c5995a3794861",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288491,
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
      "evaluated_at": 1760288491
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "b2f3a3e46453e700238e97479de0ef2553a9285ab6a80d53ede6bb748263c209"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 021000028707079
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 95, 'threshold': 50, 'total_amount': 650738315, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 94, 'first_seen': 1760285764, 'matching_hash': '67ae9df98d5fdee3'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6849877}}}