```json
{
  "id": "01a4498b67994a69",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285919,
  "host_pid": "9e6742732c60:1",
  "hash": "9678ad67ea1328a4b0a8e0022df7bfa657957af20f16c6ea0b9d990fdd5484ce",
  "cid": "QmV19678ad67ea1328a4b0a8e0022df7bfa657957af2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285919,
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
      "evaluated_at": 1760285919
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
  "sig": "ec79007d620002339370452c18f6262d9ce2329a478c75f4215eb395717bcb70"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 039274533993332
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 7, 'first_seen': 1760285765, 'matching_hash': 'a2ad50f9b8d4dabc'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '039274537', 'validation_error': 'Invalid routing number checksum'}}}