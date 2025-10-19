```json
{
  "id": "2dfa2ed055a54d50",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288407,
  "host_pid": "9e6742732c60:1",
  "hash": "388e56e88bd3c1c568cc6daae7af5d7c13989910d7c069ba5e7edbe4921c98e8",
  "cid": "QmV1388e56e88bd3c1c568cc6daae7af5d7c13989910",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288407,
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
      "evaluated_at": 1760288407
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
  "sig": "5ce65ffb4b44284d4e02d6a137499e1561723d8e522ca7d26546c83250a648f6"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 026009595707011
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 92, 'threshold': 50, 'total_amount': 633476304, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 91, 'first_seen': 1760285765, 'matching_hash': 'bce5819bd1402454'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6885612}}}