```json
{
  "id": "96a58371468209b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294663,
  "host_pid": "9e6742732c60:1",
  "hash": "fb999f4a910d897ed6b3d6f5ded07f3a2f41fc373b52426f56f4753faf2daf73",
  "cid": "QmV1fb999f4a910d897ed6b3d6f5ded07f3a2f41fc37",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294663,
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
      "evaluated_at": 1760294663
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
  "sig": "36777dc87f6d4a65291e986414d37aeaf727ff127b4d34ed2903f2c553ccdf64"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465603072
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 14639306, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285763, 'matching_hash': 'e359f7b1cd5a9343'}}}