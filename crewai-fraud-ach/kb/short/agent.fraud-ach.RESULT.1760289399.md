```json
{
  "id": "bddc4947799c7877",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289399,
  "host_pid": "9e6742732c60:1",
  "hash": "1bbfa5266d4b4797710ecdb79e4a2d40f8f2f5ce0024cac1c46a6edd494b5bec",
  "cid": "QmV11bbfa5266d4b4797710ecdb79e4a2d40f8f2f5ce",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289399,
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
      "evaluated_at": 1760289399
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
  "sig": "d7e23a1b77b9df13312a40f80e5610eeb8eaa340b3333cc0f9aef5e536dacb93"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 650095542347097
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 122, 'threshold': 50, 'total_amount': 17004726, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 121, 'first_seen': 1760285764, 'matching_hash': 'ccbd48c11c0f622e'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '650095545', 'validation_error': 'Invalid routing number checksum'}}}