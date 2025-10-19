```json
{
  "id": "612cd200b06f7999",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289694,
  "host_pid": "9e6742732c60:1",
  "hash": "8d2cb94756ee4db5dfe2dd0b0687ccb9a447389d1e9a0fe0639cc616b61b4e98",
  "cid": "QmV18d2cb94756ee4db5dfe2dd0b0687ccb9a447389d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289694,
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
      "evaluated_at": 1760289694
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
  "sig": "e4bcbd5c65e281fb2af1b8cc4da351d6913e18a7e87c8ab903118e6e0c4b5934"
}
```

Fraud detected: amount_anomaly (score: 89)
Transaction: 121000241325245
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 130, 'threshold': 50, 'total_amount': 1060755150, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 129, 'first_seen': 1760285765, 'matching_hash': '97920a0a35eda98b'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 82, 'details': {'zscore': 4.23, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8159655}}}