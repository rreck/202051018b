```json
{
  "id": "9ce758bc8a848ab5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292229,
  "host_pid": "9e6742732c60:1",
  "hash": "1ca31be3528387d320ffeca03626210edf974c093de5d6f62c864226741db1a4",
  "cid": "QmV11ca31be3528387d320ffeca03626210edf974c09",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292229,
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
      "evaluated_at": 1760292229
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "e86c79be650066fea60663b03b334f8f32bf861b3c6a53b01df8b8c2eead8d8a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000020947870
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 13022482, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285763, 'matching_hash': '1f43c37f0aae1875'}}}maly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.17, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8052182}}}