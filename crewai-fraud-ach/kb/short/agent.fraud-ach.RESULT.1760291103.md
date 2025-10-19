```json
{
  "id": "c20c9ef724cd9b87",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291103,
  "host_pid": "9e6742732c60:1",
  "hash": "e9884b5463ce7759e7c04bc9f58f5c6f697a55566189c995b981c97aef5600cc",
  "cid": "QmV1e9884b5463ce7759e7c04bc9f58f5c6f697a5556",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291103,
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
      "evaluated_at": 1760291103
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
  "sig": "325c8abb860a33fc1127a9174408b886377de7450e1576eb1cd1a9f1df861002"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461197823
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 30125965, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285763, 'matching_hash': 'c7e6425f6e43a399'}}}