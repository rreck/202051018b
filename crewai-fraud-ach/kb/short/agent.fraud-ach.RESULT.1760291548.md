```json
{
  "id": "27b7aead818a888c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291548,
  "host_pid": "9e6742732c60:1",
  "hash": "468510edc94a92449ffc74d352efaf66cca0915888a1a0f59fbf05e5d2b7a4b0",
  "cid": "QmV1468510edc94a92449ffc74d352efaf66cca09158",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291548,
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
      "evaluated_at": 1760291548
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
  "sig": "54e34a06d7802e481efc33ad26ade9e7c1afefd714f08014b3b053d800e0afeb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 56329896, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}