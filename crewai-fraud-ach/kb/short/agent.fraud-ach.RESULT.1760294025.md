```json
{
  "id": "eea0c4953119e9a8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294025,
  "host_pid": "9e6742732c60:1",
  "hash": "4bd213d53e220658ffa44544167930ecf704460c51eb7ab19016f8a2fb72eaf3",
  "cid": "QmV14bd213d53e220658ffa44544167930ecf704460c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294025,
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
      "evaluated_at": 1760294025
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
  "sig": "a1213af8ded19d61460883873b230d20223d8d11b1dc8fcddc3ec8734c21b629"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243741176
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 69992450, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285763, 'matching_hash': 'e78a513bf0bcec2f'}}}