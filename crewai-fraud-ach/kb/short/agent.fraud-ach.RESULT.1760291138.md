```json
{
  "id": "aca1d897ca5cb2bc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291138,
  "host_pid": "9e6742732c60:1",
  "hash": "daa00ca85ccf2ece9d76a4564ba0cf5381fdec66adb21f221d18c9621973578f",
  "cid": "QmV1daa00ca85ccf2ece9d76a4564ba0cf5381fdec66",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291138,
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
      "evaluated_at": 1760291138
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
  "sig": "e51795b64310e7aa3288d8f7c6110f9e157b828488d4ce13c55f1d5e7f081f88"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154932354
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285763, 'matching_hash': '0dfd62e893bef2e1'}}}5763, 'matching_hash': 'b69a4a680810c6df'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '244096997', 'validation_error': 'Invalid routing number checksum'}}}