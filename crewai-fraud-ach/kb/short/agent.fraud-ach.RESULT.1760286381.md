```json
{
  "id": "5f4a7905db64cfd6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286381,
  "host_pid": "9e6742732c60:1",
  "hash": "d02bb13ba6bf15308cdd4c5776dcb493db8675318a45110af5095657c42a4564",
  "cid": "QmV1d02bb13ba6bf15308cdd4c5776dcb493db867531",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286381,
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
      "evaluated_at": 1760286381
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
  "sig": "a2e7297bfa4ab0b9e9cd84904fca05a140970c914c18c7454a7597b39ffb3d7d"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 507153179781967
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 22, 'first_seen': 1760285765, 'matching_hash': 'b9dbbc4d232307f2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '507153176', 'validation_error': 'Invalid routing number checksum'}}}