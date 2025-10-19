```json
{
  "id": "104246b2949b8d40",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288242,
  "host_pid": "9e6742732c60:1",
  "hash": "18b4ee672d42bd899c080e21ad1ce1ee060ebad833a71fa592224053ff9839f2",
  "cid": "QmV118b4ee672d42bd899c080e21ad1ce1ee060ebad8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288242,
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
      "evaluated_at": 1760288242
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
  "sig": "30bf0a59cb5ab84c2556f2597f000d2591b92a553d1b1e68db3a63ec516d6eb4"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 111000024639540
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 87, 'threshold': 50, 'total_amount': 667467654, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 86, 'first_seen': 1760285765, 'matching_hash': '9eefc6a12f8b62a3'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7672042}}}