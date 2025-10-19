```json
{
  "id": "bcfeb790ee8ded1a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293188,
  "host_pid": "9e6742732c60:1",
  "hash": "9d450d2fc1b2dfaf9f576cdbe8c8aa0dc5e4a844cad21f21179c8ca01a6bfbd1",
  "cid": "QmV19d450d2fc1b2dfaf9f576cdbe8c8aa0dc5e4a844",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293188,
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
      "evaluated_at": 1760293188
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
  "sig": "48d1eaba9702b138e32bcf2991396112a8cff2a8b4416dd48052694a05f7b6fa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037423947
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 42536313, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285763, 'matching_hash': '5528b0ca47a44e30'}}}