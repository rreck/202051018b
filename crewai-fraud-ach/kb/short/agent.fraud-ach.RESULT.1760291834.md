```json
{
  "id": "f738ccbf9b05f2c4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291834,
  "host_pid": "9e6742732c60:1",
  "hash": "ed4061b7d8898266f45dfc1c309d095517fcbc37a08cd325790a36400d0dd1d5",
  "cid": "QmV1ed4061b7d8898266f45dfc1c309d095517fcbc37",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291834,
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
      "evaluated_at": 1760291834
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
  "sig": "cc195626bc7c425074dce8c64366b4a2f12b9f8b69218388b2cbde989560b807"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 026009594219462
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 939368944, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285763, 'matching_hash': '4d9d7d0d036b9510'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5105266}}}}