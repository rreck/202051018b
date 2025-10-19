```json
{
  "id": "d71634d98f85764c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290748,
  "host_pid": "9e6742732c60:1",
  "hash": "b18e84c3fe378d18bb2a02b47f1939159daec8b8b2d8f79c6f1c9fe9ec7ea547",
  "cid": "QmV1b18e84c3fe378d18bb2a02b47f1939159daec8b8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290748,
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
      "evaluated_at": 1760290748
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
  "sig": "e0a22095e1258fc699c32073a95746418c4795d05c616dcce09a68991f408d3f"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 122105155421893
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 799910866, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285765, 'matching_hash': 'b50b947262955843'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5062727}}}