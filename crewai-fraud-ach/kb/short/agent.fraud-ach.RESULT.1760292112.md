```json
{
  "id": "16b8f939b07cd934",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292112,
  "host_pid": "9e6742732c60:1",
  "hash": "84a0beda6ba6dd73ea7e2f042aab13bae1836a48d8137349d6dc2d01777ac20b",
  "cid": "QmV184a0beda6ba6dd73ea7e2f042aab13bae1836a48",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292112,
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
      "evaluated_at": 1760292112
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
  "sig": "ef93bcfc34366174c12592dc35ffb7062a11d16d41417aedfbcb20a49cc5ee7e"
}
```

Fraud detected: amount_anomaly (score: 92)
Transaction: 063100273946283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 1843081700, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285765, 'matching_hash': 'ff0c3c22534c93d5'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 91, 'details': {'zscore': 5.11, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9700430}}}