```json
{
  "id": "f16941b3c8b6d200",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289358,
  "host_pid": "9e6742732c60:1",
  "hash": "8707763ab643ee79394e267829b43f6bc9a166116d3ffbb86998f7b2ba254491",
  "cid": "QmV18707763ab643ee79394e267829b43f6bc9a16611",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289358,
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
      "evaluated_at": 1760289359
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
  "sig": "ff0ee2c56a571a325794f08be604d7f39be6c504be91d162e974d768f1a5167b"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 060557484693193
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 121, 'threshold': 50, 'total_amount': 51837973, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 120, 'first_seen': 1760285763, 'matching_hash': 'db8aeeee2135ece1'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '060557489', 'validation_error': 'Invalid routing number checksum'}}}