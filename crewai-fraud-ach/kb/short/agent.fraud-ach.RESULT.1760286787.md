```json
{
  "id": "ad885d26dfbe163e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286787,
  "host_pid": "9e6742732c60:1",
  "hash": "4e1275e5fe7894eb312ac9789a90988ef24136d7c8f5fb27b76553f1e0c5c981",
  "cid": "QmV14e1275e5fe7894eb312ac9789a90988ef24136d7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286787,
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
      "evaluated_at": 1760286787
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
  "sig": "420206757d2959e76db1c0463b975903fa78e4523ce0c52f2feb32194819571b"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000037578651
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 36, 'first_seen': 1760285763, 'matching_hash': '25cb229761d99325'}}}