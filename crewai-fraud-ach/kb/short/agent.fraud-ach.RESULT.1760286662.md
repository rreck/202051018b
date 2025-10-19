```json
{
  "id": "7db126ee823f6175",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286662,
  "host_pid": "9e6742732c60:1",
  "hash": "2846aa4be3f4997a51d4f9f446fa23a503ea592e3717a2b83a96b16b9cf34b1b",
  "cid": "QmV12846aa4be3f4997a51d4f9f446fa23a503ea592e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286662,
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
      "evaluated_at": 1760286662
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "e440309daf524deda9d4e1ad6aa1006f0d22de5bca8e17f8f288deef7b6609b4"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 561028999821965
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 32, 'first_seen': 1760285763, 'matching_hash': '09f745cfd1242827'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '561028991', 'validation_error': 'Invalid routing number checksum'}}}