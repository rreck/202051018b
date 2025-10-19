```json
{
  "id": "4aab98c7ccd31d26",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289875,
  "host_pid": "9e6742732c60:1",
  "hash": "699bb78e378eaff278e02bccbec368d4ea9261c95426aaec8d88ad8f07766c3b",
  "cid": "QmV1699bb78e378eaff278e02bccbec368d4ea9261c9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289875,
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
      "evaluated_at": 1760289875
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
  "sig": "bbb11a32924ed8bdd8067fe2668d1852362629c47a42e443c7c9bc156d19e7f9"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 026009595707011
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 135, 'threshold': 50, 'total_amount': 929557620, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 134, 'first_seen': 1760285765, 'matching_hash': 'bce5819bd1402454'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.51, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6885612}}}