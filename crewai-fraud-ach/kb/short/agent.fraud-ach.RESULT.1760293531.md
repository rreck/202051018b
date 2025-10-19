```json
{
  "id": "98422c61ee6f1686",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293531,
  "host_pid": "9e6742732c60:1",
  "hash": "b34836a37ed02a2678356cc85f0605b5e43aede398c2ce63c86983a217352b3a",
  "cid": "QmV1b34836a37ed02a2678356cc85f0605b5e43aede3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293531,
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
      "evaluated_at": 1760293531
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
  "sig": "4f5d856e63d91af44580d170ac1cb2f4d426e5a0537cc0ea01402b6e1a14dff5"
}
```

Fraud detected: amount_anomaly (score: 90)
Transaction: 044000033143138
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 1958257620, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285764, 'matching_hash': '6d0d609b65d243f3'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 86, 'details': {'zscore': 4.66, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8901171}}}