```json
{
  "id": "448b3a4e41004af9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292691,
  "host_pid": "9e6742732c60:1",
  "hash": "3566bbf4d86666b3e2a84b8abf0682d930a3d1cffc47a3891d4834c28b00f534",
  "cid": "QmV13566bbf4d86666b3e2a84b8abf0682d930a3d1cf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292691,
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
      "evaluated_at": 1760292691
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
  "sig": "d0d72447c2065ec22833290baaf5dc11bf79da003a27b727fce741b3155f722f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596829725
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 67084192, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285763, 'matching_hash': '14fa64c7f7d5a53d'}}}maly': {'fraud_detected': True, 'risk_score': 86, 'details': {'zscore': 4.68, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8942822}}}