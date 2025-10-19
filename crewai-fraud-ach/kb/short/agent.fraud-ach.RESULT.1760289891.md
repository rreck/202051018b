```json
{
  "id": "95ec7820e4f03f9e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289891,
  "host_pid": "9e6742732c60:1",
  "hash": "20fae23b1681230d6e76ec99344f32cff7f08c583626393bd409415a5e809937",
  "cid": "QmV120fae23b1681230d6e76ec99344f32cff7f08c58",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289891,
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
      "evaluated_at": 1760289892
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
  "sig": "c85a91280bf901c997bfb05354be17ea2fc57caaeb15a503ebbf21a45b5aedcd"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 568426902254568
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 136, 'threshold': 50, 'total_amount': 52486752, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 135, 'first_seen': 1760285763, 'matching_hash': '885fc97ad7583ad3'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '568426909', 'validation_error': 'Invalid routing number checksum'}}}