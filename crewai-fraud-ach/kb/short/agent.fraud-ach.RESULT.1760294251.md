```json
{
  "id": "fd836ae0080a3024",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294251,
  "host_pid": "9e6742732c60:1",
  "hash": "e2ba820ed71d2ee60fccd9405c613880f397cd1a1fcb972280ca379c9a283006",
  "cid": "QmV1e2ba820ed71d2ee60fccd9405c613880f397cd1a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294251,
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
      "evaluated_at": 1760294251
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
  "sig": "479f23a0a08d8826e50c1d33b3fc635e05463ed4517193516fa186f032a4df26"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 121000249844926
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 1229342868, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285765, 'matching_hash': '4f8c06dc9d4c212b'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5253602}}}