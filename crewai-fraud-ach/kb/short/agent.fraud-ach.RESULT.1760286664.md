```json
{
  "id": "896d9bd44637dff2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286664,
  "host_pid": "9e6742732c60:1",
  "hash": "da5554dfa41cc09de8a9e8e7eeb5515211a2f0ff59468823516a39c94cf89537",
  "cid": "QmV1da5554dfa41cc09de8a9e8e7eeb5515211a2f0ff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286664,
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
      "evaluated_at": 1760286664
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
  "sig": "530bdeb99506f9238170b304040f9a2e15a24b893a39f028bf6b24e7e89bf59f"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 868351858992484
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 14439150, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 32, 'first_seen': 1760285763, 'matching_hash': '153716104ce1f6b1'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '868351851', 'validation_error': 'Invalid routing number checksum'}}}