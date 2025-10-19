```json
{
  "id": "1bfd0dccbeccbb39",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290240,
  "host_pid": "9e6742732c60:1",
  "hash": "622b7499af97ba08d28e3e41238c899490fa12c26eb20b7416127570032f3121",
  "cid": "QmV1622b7499af97ba08d28e3e41238c899490fa12c2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290240,
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
      "evaluated_at": 1760290240
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
  "sig": "440694d30f3d013a3aaa2ed0a1ad0cd0b881beae64e462ab875701ea54fe2ed7"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 044000039260642
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 1236647048, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760284979, 'matching_hash': 'a7542f9d69c5b02c'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5595688}}}