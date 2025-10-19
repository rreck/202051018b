```json
{
  "id": "37c467aca97f405e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286007,
  "host_pid": "9e6742732c60:1",
  "hash": "664a322244b838feebfbaeb443e94fa20632a80808db885d5b3bacd55e626b04",
  "cid": "QmV1664a322244b838feebfbaeb443e94fa20632a808",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286007,
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
      "evaluated_at": 1760286007
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
  "sig": "c26b81ab2dc4ad0917f6f5e02baeac0b108338c4948bb7940a118bb3a8c93d06"
}
```

Fraud detected: amount_anomaly (score: 76)
Transaction: 044000033143138
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 97912881, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 10, 'first_seen': 1760285764, 'matching_hash': '6d0d609b65d243f3'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 73, 'details': {'zscore': 3.35, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8901171}}}