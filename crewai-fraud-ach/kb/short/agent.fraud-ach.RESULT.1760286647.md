```json
{
  "id": "96b1368d416e9961",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286647,
  "host_pid": "9e6742732c60:1",
  "hash": "49f7b2e482db216a925385f8a236fbd5fa7a6cf3fd1e16eed8fbbfac5d42b0dc",
  "cid": "QmV149f7b2e482db216a925385f8a236fbd5fa7a6cf3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286647,
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
      "evaluated_at": 1760286647
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
  "sig": "868c34d552ac04f127f70791c9371005c136c1af0c25155d08a963b003322141"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 264316140004295
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 12453856, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 31, 'first_seen': 1760285765, 'matching_hash': 'f346c773c62e50ad'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '264316140', 'validation_error': 'Invalid routing number checksum'}}}