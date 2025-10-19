```json
{
  "id": "ce302e908bdb1fd4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287276,
  "host_pid": "9e6742732c60:1",
  "hash": "4272ba1f0ebcbe7611092b84532a30153ebd17b6e120002ed8f098c90ebfc80a",
  "cid": "QmV14272ba1f0ebcbe7611092b84532a30153ebd17b6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287276,
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
      "evaluated_at": 1760287276
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_high"
  ],
  "sig": "849a03b98ef9044bda17f170282de943b58d0d52bfe5f314b62f0f351cd261c2"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 111000026237439
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 54, 'threshold': 50, 'total_amount': 294954858, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 53, 'first_seen': 1760285765, 'matching_hash': '88704d1e07f02084'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5462127}}}