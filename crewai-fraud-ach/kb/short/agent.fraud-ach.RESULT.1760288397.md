```json
{
  "id": "1874bfab8335a22d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288397,
  "host_pid": "9e6742732c60:1",
  "hash": "7fa4ad38ebf09148dae1e688cdf8345ce7b4ebd0a5eec0c5840f6ca5c48e1e07",
  "cid": "QmV17fa4ad38ebf09148dae1e688cdf8345ce7b4ebd0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288397,
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
      "evaluated_at": 1760288397
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
  "sig": "7efe9047419679fb0c766d2ba83577fa7b0e4345c2290bd3b80bac464bc3956e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037507630
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 92, 'threshold': 50, 'total_amount': 33188448, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 91, 'first_seen': 1760285763, 'matching_hash': '9b4ed9a2b11bf5fa'}}}