```json
{
  "id": "3ad0f22f40a8b8ad",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290699,
  "host_pid": "9e6742732c60:1",
  "hash": "6fd29bc72cc82138391aa9863e8c5b41154289cc756f12737c18d54a5000222d",
  "cid": "QmV16fd29bc72cc82138391aa9863e8c5b41154289cc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290699,
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
      "evaluated_at": 1760290699
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
  "sig": "8d79e852d6d2840d5c1ceb06f7f52b9e97fb893fc9240700032288a1f59bd3f8"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 063100270473682
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 1498973985, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285763, 'matching_hash': 'dcfb2900505c6ddc'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 90, 'details': {'zscore': 5.02, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9547605}}}