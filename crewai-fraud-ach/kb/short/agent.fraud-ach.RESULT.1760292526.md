```json
{
  "id": "55a0cc57f4dc54b6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292526,
  "host_pid": "9e6742732c60:1",
  "hash": "a714f20bc68501916ecbca31e12d8a438c9e560da96523373877473dab0f6b93",
  "cid": "QmV1a714f20bc68501916ecbca31e12d8a438c9e560d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292526,
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
      "evaluated_at": 1760292526
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
  "sig": "af2bd77d0d859ed4b491f13b3334927e96871820e31a1e63eeee834fc7432080"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247383202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 79252745, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285765, 'matching_hash': '32929947211460fd'}}}