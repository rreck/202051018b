```json
{
  "id": "0af327b357d5cb33",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289783,
  "host_pid": "9e6742732c60:1",
  "hash": "3064f7d6cf81d163452772dba5b6f930f8af8a9890012ca219c26d9f60abc101",
  "cid": "QmV13064f7d6cf81d163452772dba5b6f930f8af8a98",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289783,
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
      "evaluated_at": 1760289783
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
  "sig": "f06fff84739392cb496418ac693605c1903179217f63751cc7f89dfcdad9f588"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022959454
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50, 'total_amount': 20005062, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760285763, 'matching_hash': 'd9e1e1b77e5bc9b7'}}}