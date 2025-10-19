```json
{
  "id": "f97eefa7bb22c4c3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286982,
  "host_pid": "9e6742732c60:1",
  "hash": "dc803470e2cf22083c446a346c5fa2d2713e51f2e3cd91bbb5a0a7327c8b26bb",
  "cid": "QmV1dc803470e2cf22083c446a346c5fa2d2713e51f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286982,
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
      "evaluated_at": 1760286982
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "9392ced04d57ce0190525e47e7fa84cba5311be20c0056d7bcf4e646d6057331"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000245084656
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 15356528, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 43, 'first_seen': 1760285763, 'matching_hash': '11924a0da29b01ce'}}}aly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6602570}}}