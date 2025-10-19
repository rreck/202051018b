```json
{
  "id": "063a9662cbe1a715",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289816,
  "host_pid": "9e6742732c60:1",
  "hash": "848c82decbc19b65052792489db6eeb4e4a7c8ec6c49da01bdd9d8ba8e5a887b",
  "cid": "QmV1848c82decbc19b65052792489db6eeb4e4a7c8ec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289816,
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
      "evaluated_at": 1760289816
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
  "sig": "934bf9c383f1cba67bfb6332938a0a8eccc5546cab5a023454ece0c1b35ed1ba"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 561028999821965
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50, 'total_amount': 18758526, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285763, 'matching_hash': '09f745cfd1242827'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '561028991', 'validation_error': 'Invalid routing number checksum'}}}