```json
{
  "id": "f924a5406e62b709",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293511,
  "host_pid": "9e6742732c60:1",
  "hash": "c0466edff5b7ec9770a6b4d9ee1d9d4687c00f5675285b569b203cc79cff1439",
  "cid": "QmV1c0466edff5b7ec9770a6b4d9ee1d9d4687c00f56",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293511,
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
      "evaluated_at": 1760293511
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
  "sig": "540ae4aa8b9657bfef6f36a6c0612fd0dcf5e9d9651a6d43f7a3a05dcb1ab79e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278619879
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 74515540, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285763, 'matching_hash': 'bfc334a18daf8fbf'}}}unt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}