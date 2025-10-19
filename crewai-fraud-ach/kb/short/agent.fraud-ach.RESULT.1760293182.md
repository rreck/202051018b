```json
{
  "id": "9fac39f6e170a6ce",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293182,
  "host_pid": "9e6742732c60:1",
  "hash": "92279d8c793024424f843de306ab42bc237909e0f3406dae22fef3e8132374ea",
  "cid": "QmV192279d8c793024424f843de306ab42bc237909e0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293182,
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
      "evaluated_at": 1760293182
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
  "sig": "8426dbab8b4e524f75f0575e996b874073dc22e14f16f647c9db3ecd3f8b68d7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461869062
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 105815205, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285763, 'matching_hash': '24ed6b728fb62d75'}}}