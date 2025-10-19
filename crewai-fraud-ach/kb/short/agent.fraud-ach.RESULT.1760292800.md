```json
{
  "id": "f80fc3c6534d5cd4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292800,
  "host_pid": "9e6742732c60:1",
  "hash": "ea0386a6e819bf7988bfe058e10a91e3ab2f7097f57eb506033d5861336e9604",
  "cid": "QmV1ea0386a6e819bf7988bfe058e10a91e3ab2f7097",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292800,
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
      "evaluated_at": 1760292800
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
  "sig": "816dc2cb26d53998d1a6cdf26222ee999a7a0b1fe1a3d07c4f1950cd91e2de5d"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 039274533993332
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 33407415, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285765, 'matching_hash': 'a2ad50f9b8d4dabc'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '039274537', 'validation_error': 'Invalid routing number checksum'}}}