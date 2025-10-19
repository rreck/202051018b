```json
{
  "id": "bd155f864ad2c4dc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292924,
  "host_pid": "9e6742732c60:1",
  "hash": "0a3b1c51064e97118c6cd6dfe267cb275c55c52b4c091b260ceacc8c43368122",
  "cid": "QmV10a3b1c51064e97118c6cd6dfe267cb275c55c52b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292924,
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
      "evaluated_at": 1760292924
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
  "sig": "cfd8091eff179be27a4a9384f603a92adffa7a47be4b899aee3329b35d65e2bb"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 013419647478508
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 52688064, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285763, 'matching_hash': 'f6be81dddddc1883'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '013419643', 'validation_error': 'Invalid routing number checksum'}}}