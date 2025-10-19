```json
{
  "id": "26b71be0047431d2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292409,
  "host_pid": "9e6742732c60:1",
  "hash": "142934c456abde13c326b256114de8e9e43f17f6d189f877550ca62bad216695",
  "cid": "QmV1142934c456abde13c326b256114de8e9e43f17f6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292409,
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
      "evaluated_at": 1760292409
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
  "sig": "e48fd71477de7fdbf64025ec6f46d75893172caa8bf881bb9c7e15850188ca50"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 111000023855884
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 1853945133, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285763, 'matching_hash': '29f4fac8ca9c8442'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 89, 'details': {'zscore': 4.95, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9410889}}}