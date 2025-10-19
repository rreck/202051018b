```json
{
  "id": "59f9f4ea5b28ce00",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292734,
  "host_pid": "9e6742732c60:1",
  "hash": "a8875e81283019598160555636e5eb9d890797235983b43621f1b2c61164e08c",
  "cid": "QmV1a8875e81283019598160555636e5eb9d89079723",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292734,
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
      "evaluated_at": 1760292734
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
  "sig": "31c0b419c91e57a97adca2d253a6bde91c87f42656a74e90115b450c0ba57c92"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 868351858992484
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 89260200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285763, 'matching_hash': '153716104ce1f6b1'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '868351851', 'validation_error': 'Invalid routing number checksum'}}}