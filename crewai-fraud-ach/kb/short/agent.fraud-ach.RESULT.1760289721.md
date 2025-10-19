```json
{
  "id": "eb9c29c619447b1e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289721,
  "host_pid": "9e6742732c60:1",
  "hash": "8cf902ce285f9251b5b02e6cd4e2e0335467b23004055909379be95d8760de33",
  "cid": "QmV18cf902ce285f9251b5b02e6cd4e2e0335467b230",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289721,
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
      "evaluated_at": 1760289721
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
  "sig": "77cf6c1c6cafd2d0f9264238a1ecd39ba19a7a21646681bd0fb0b8733dcc8c0e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278037585
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50, 'total_amount': 13914296, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285763, 'matching_hash': '27cb7a10328c75d5'}}}