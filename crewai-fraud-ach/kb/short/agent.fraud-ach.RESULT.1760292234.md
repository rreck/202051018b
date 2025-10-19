```json
{
  "id": "8e2d86a3dcf5d47a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292234,
  "host_pid": "9e6742732c60:1",
  "hash": "30f9f69f4fcb80feafa71a527421034b2e481420c7e6ef835e37d47445eac006",
  "cid": "QmV130f9f69f4fcb80feafa71a527421034b2e481420",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292234,
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
      "evaluated_at": 1760292234
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
  "sig": "8f27344a015d7c9cd2326b22925a17e602aed046bdab6d24b1a1ee9d4dccc9cc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248764263
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 70097214, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285763, 'matching_hash': '9f14c95be52dc67f'}}}