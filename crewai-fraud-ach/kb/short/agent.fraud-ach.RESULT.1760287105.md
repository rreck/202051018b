```json
{
  "id": "97b45cc3acbddc55",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287105,
  "host_pid": "9e6742732c60:1",
  "hash": "320df52832b145c924cdc4a1cc870ef0d900a4024d7a5e432e24ed268a34d1e4",
  "cid": "QmV1320df52832b145c924cdc4a1cc870ef0d900a402",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287105,
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
      "evaluated_at": 1760287105
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
  "sig": "8c6015cc1ef44484b4cc73458673a5b5a5a306060fbe25199aa16d264c648444"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 031201467532863
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 264688272, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 47, 'first_seen': 1760285764, 'matching_hash': 'b320222423bba5e6'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5514339}}}