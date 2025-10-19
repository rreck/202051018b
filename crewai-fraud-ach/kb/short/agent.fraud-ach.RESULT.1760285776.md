```json
{
  "id": "eaffb11c975c84da",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285776,
  "host_pid": "9e6742732c60:1",
  "hash": "04a4aff49fb1d4418e02139d76e28f7b012e2ec80116ce285ee1a15e63d72b43",
  "cid": "QmV104a4aff49fb1d4418e02139d76e28f7b012e2ec8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285776,
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
      "evaluated_at": 1760285776
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
  "sig": "07132410777f92894fe1a44713b807d397fd4314a06d8b626baa1c685eaf7124"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000023536829
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 1, 'first_seen': 1760285763, 'matching_hash': 'cf71240b8169078c'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '085520764', 'validation_error': 'Invalid routing number checksum'}}}