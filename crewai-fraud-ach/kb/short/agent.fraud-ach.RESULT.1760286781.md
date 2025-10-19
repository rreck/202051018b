```json
{
  "id": "04f1cc11b39e3cdd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286781,
  "host_pid": "9e6742732c60:1",
  "hash": "35b7041235f8b6d21c3627bb30776bbe4c7b499b6092df13cec2fb12f3be563c",
  "cid": "QmV135b7041235f8b6d21c3627bb30776bbe4c7b499b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286781,
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
      "evaluated_at": 1760286781
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
  "sig": "caff99aa530fc0647c3825fb6fcfe73ad62e60d2fd461f4e23b27a8f16481d8f"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000031117260
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 36, 'first_seen': 1760285763, 'matching_hash': '467ec1c9bc787c3f'}}}