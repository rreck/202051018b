```json
{
  "id": "1253c8197d9f076f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289712,
  "host_pid": "9e6742732c60:1",
  "hash": "dee4e95e4ad4a5b5e6021c365ea278b6b9029d91d8518195277ec932636a379a",
  "cid": "QmV1dee4e95e4ad4a5b5e6021c365ea278b6b9029d91",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289712,
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
      "evaluated_at": 1760289712
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
  "sig": "0dc825e44968ed35a190cfc2c150d5be89a8e134a35037afffaa7dd9b640bec7"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 026009595171446
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50, 'total_amount': 848674854, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285763, 'matching_hash': '6f6a57bfd56698c7'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 72, 'details': {'zscore': 3.28, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6478434}}}