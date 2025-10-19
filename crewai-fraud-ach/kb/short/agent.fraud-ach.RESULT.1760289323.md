```json
{
  "id": "534c9b2067df7a28",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289323,
  "host_pid": "9e6742732c60:1",
  "hash": "d00823a236087cfad862f1847cc487334c9b24e36d5743666928c43929a91e40",
  "cid": "QmV1d00823a236087cfad862f1847cc487334c9b24e3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289323,
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
      "evaluated_at": 1760289323
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "c8f572fbfe46f3491ed53438b0cb2e2eeaf182255a02d524402d76af8e5b055f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025820321
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 120, 'threshold': 50, 'total_amount': 30938160, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 119, 'first_seen': 1760285763, 'matching_hash': 'cf65bb25527720c5'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '060557489', 'validation_error': 'Invalid routing number checksum'}}}