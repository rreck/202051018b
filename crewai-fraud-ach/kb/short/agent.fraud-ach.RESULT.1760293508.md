```json
{
  "id": "4a612776a80df968",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293508,
  "host_pid": "9e6742732c60:1",
  "hash": "0435fc501d02929af05249f42b71fa0864cc9aa60a23492281bf1074c1d9902b",
  "cid": "QmV10435fc501d02929af05249f42b71fa0864cc9aa6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293508,
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
      "evaluated_at": 1760293508
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
  "sig": "3d2393647c76811a1b1e32936a05a067a45a1f5de409c84c575bdd51c1200049"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242172457
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 103657400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285763, 'matching_hash': '180325de6151a8c9'}}}