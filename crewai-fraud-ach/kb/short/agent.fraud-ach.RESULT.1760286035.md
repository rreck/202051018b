```json
{
  "id": "b32a2c3bb32ad6e1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286035,
  "host_pid": "9e6742732c60:1",
  "hash": "9a58e14f2eea36d05bfdf80e452b67c6ed242471551f49524dba91e33264ec73",
  "cid": "QmV19a58e14f2eea36d05bfdf80e452b67c6ed242471",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286035,
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
      "evaluated_at": 1760286035
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
  "sig": "15739e4d9c64e3aec13d5e01e369165f6e99d374063ad0f777b9561e7b8ae866"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 111000024639540
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 92064504, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 11, 'first_seen': 1760285765, 'matching_hash': '9eefc6a12f8b62a3'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7672042}}}