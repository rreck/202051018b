```json
{
  "id": "05163a4498bce7ef",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289640,
  "host_pid": "9e6742732c60:1",
  "hash": "bc00f1feb28ad949253e37a6bf790d70e865248666547939a4bb95e410fa141a",
  "cid": "QmV1bc00f1feb28ad949253e37a6bf790d70e8652486",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289640,
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
      "evaluated_at": 1760289640
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
  "sig": "86bc7c4a7c8bd8a4acd115ac0cd778f65717916b53f8b2b33751a86ae0ddc15b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248193290
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50, 'total_amount': 25564704, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760285763, 'matching_hash': '8925647bbeca80db'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '041887155', 'validation_error': 'Invalid routing number checksum'}}}