```json
{
  "id": "74ddac42d8e7529d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291279,
  "host_pid": "9e6742732c60:1",
  "hash": "29b36051decfe57d6fde9e66f91492e5a334eebcdbea2843ca1c9c5524236415",
  "cid": "QmV129b36051decfe57d6fde9e66f91492e5a334eebc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291279,
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
      "evaluated_at": 1760291280
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
  "sig": "0df971f1fa460a1b74021a06c0a338b1e3469bcde401267683c8e23c596d4ac4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464946217
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 247, 'threshold': 50, 'total_amount': 84064721, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 246, 'first_seen': 1760284979, 'matching_hash': '76eefa6b67e55304'}}}