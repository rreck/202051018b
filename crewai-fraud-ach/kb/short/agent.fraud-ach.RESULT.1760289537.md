```json
{
  "id": "55b44da3db2739d0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289537,
  "host_pid": "9e6742732c60:1",
  "hash": "e6798664db12fa65285e6bb4d66373f88ce07f1494cac03f439dea03ebf68e38",
  "cid": "QmV1e6798664db12fa65285e6bb4d66373f88ce07f14",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289537,
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
      "evaluated_at": 1760289537
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
  "sig": "5e911fd66efe32d62aa4896b04e632aba70befd60f7a9ffb610847350ef172ce"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460939533
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 126, 'threshold': 50, 'total_amount': 41284908, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760285763, 'matching_hash': '9fc2d1aa6be5a150'}}}