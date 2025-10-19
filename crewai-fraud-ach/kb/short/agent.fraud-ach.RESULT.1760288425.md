```json
{
  "id": "e23be915a4eba078",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288425,
  "host_pid": "9e6742732c60:1",
  "hash": "f182b0d8322b168a9c396cb26a580661933cc8f04df7041ca9b090b21b03eff0",
  "cid": "QmV1f182b0d8322b168a9c396cb26a580661933cc8f0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288425,
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
      "evaluated_at": 1760288425
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
  "sig": "ec03a825446c82c9a91ed4444e2c99a1da49e23e5a4019669107c1a06f036799"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 372851334846795
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 93, 'threshold': 50, 'total_amount': 45748374, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 92, 'first_seen': 1760285763, 'matching_hash': 'e24b6b5408d67f01'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '372851336', 'validation_error': 'Invalid routing number checksum'}}}