```json
{
  "id": "08416af03aae5ce6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289369,
  "host_pid": "9e6742732c60:1",
  "hash": "c6725855552b8e2f9cd8007ba28598ded45ec84262d45ac536fc7f16bf0e0bd3",
  "cid": "QmV1c6725855552b8e2f9cd8007ba28598ded45ec842",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289369,
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
      "evaluated_at": 1760289369
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
  "sig": "52625a7b031bf1265ce1e9c047e55e7d8cbb661a17938cec89a335fc4841e463"
}
```

Fraud detected: amount_anomaly (score: 89)
Transaction: 122105150198952
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 121, 'threshold': 50, 'total_amount': 1008465546, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 120, 'first_seen': 1760285763, 'matching_hash': '35a36fb353493cca'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 83, 'details': {'zscore': 4.33, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8334426}}}