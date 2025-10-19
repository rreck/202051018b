```json
{
  "id": "89386a3c28d2356f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289375,
  "host_pid": "9e6742732c60:1",
  "hash": "fee4fd624656778c4c141ab946c5e5a6f60a8e81b69e6b9570294f6183b8178d",
  "cid": "QmV1fee4fd624656778c4c141ab946c5e5a6f60a8e81",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289375,
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
      "evaluated_at": 1760289375
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
  "sig": "b4205763b9046856f212dc1bdebeda6a72523157a1ae055baa5eb726a0a7a481"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597164999
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 121, 'threshold': 50, 'total_amount': 21684410, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 120, 'first_seen': 1760285765, 'matching_hash': 'b2fd55917469a01e'}}}