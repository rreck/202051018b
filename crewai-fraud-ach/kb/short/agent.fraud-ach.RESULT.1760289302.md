```json
{
  "id": "9b9a1e973a4cd07c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289302,
  "host_pid": "9e6742732c60:1",
  "hash": "71ce917e3e531bcf0f5425130b3523d63a4ee27a788eb78b533dd6fd203701fc",
  "cid": "QmV171ce917e3e531bcf0f5425130b3523d63a4ee27a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289302,
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
      "evaluated_at": 1760289302
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
  "sig": "a9e4656904f4c7770161ff1d99bf6a748b131a398a393d2eff6922351bb1840d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029964192
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 119, 'threshold': 50, 'total_amount': 36105195, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 118, 'first_seen': 1760285764, 'matching_hash': '3fa9c762fe00e5a2'}}}