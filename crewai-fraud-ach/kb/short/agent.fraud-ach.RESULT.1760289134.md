```json
{
  "id": "1e494bd80a595a41",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289134,
  "host_pid": "9e6742732c60:1",
  "hash": "d42dc1ed120c35d2b99100294dae1c075f959e095dabb9c91b8df5994ef5747b",
  "cid": "QmV1d42dc1ed120c35d2b99100294dae1c075f959e09",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289134,
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
      "evaluated_at": 1760289134
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
  "sig": "8ae27e704d699b714ed90079396c3907bf5b3b516a27c41840d0b7cd4b593007"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465368597
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 114, 'threshold': 50, 'total_amount': 28356132, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 113, 'first_seen': 1760285765, 'matching_hash': 'f57f84d557436d23'}}}