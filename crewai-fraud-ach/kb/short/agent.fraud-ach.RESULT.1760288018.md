```json
{
  "id": "2e9141309189b315",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288018,
  "host_pid": "9e6742732c60:1",
  "hash": "97b94aa45b9aef621cfd2fe8faf094318d7920d1ab064a412b97d7fcc00d9dbe",
  "cid": "QmV197b94aa45b9aef621cfd2fe8faf094318d7920d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288018,
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
      "evaluated_at": 1760288018
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
  "sig": "1b6e7e42e0b7b380d6f28426bffbbfd2e84aaac20982d19bb6474780153a612e"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 122105155084324
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 80, 'threshold': 50, 'total_amount': 550030080, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 79, 'first_seen': 1760285763, 'matching_hash': '91e9478c27780a65'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6875376}}} {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9410889}}}