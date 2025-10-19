```json
{
  "id": "4d5715ecfe8df5ff",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294783,
  "host_pid": "9e6742732c60:1",
  "hash": "ac375c15985bb65ad41a31b9e34e28047eed090a8e5d74bb09b6b79eedd60ddd",
  "cid": "QmV1ac375c15985bb65ad41a31b9e34e28047eed090a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294783,
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
      "evaluated_at": 1760294783
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
  "sig": "d29eefc2b66e94c0f0398a1e4a0ffb7aa3708e24a1c5a9020098450d4348adb1"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 063100275328879
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 1367553144, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285764, 'matching_hash': '9f5415d10b328afc'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5604726}}}