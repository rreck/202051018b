```json
{
  "id": "fd39d4ed10909fe6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289642,
  "host_pid": "9e6742732c60:1",
  "hash": "eca9c65734f6f2f6b4cb239c0096add1a9dd6b80aed6b161b8ccbd0784bb1edc",
  "cid": "QmV1eca9c65734f6f2f6b4cb239c0096add1a9dd6b80",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289642,
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
      "evaluated_at": 1760289642
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
  "sig": "e98400ef390f6910b49e17ab30fef0cbbbdde515bd5d0efe16e02b83bb4f2254"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242260871
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50, 'total_amount': 42937134, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760285764, 'matching_hash': '677d45847b06d7dd'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '244163284', 'validation_error': 'Invalid routing number checksum'}}}