```json
{
  "id": "dcf7f4ac517be750",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285844,
  "host_pid": "9e6742732c60:1",
  "hash": "e64a3c6ee048e89286302a5b0c4f4742f6acde17c392fcb6d4bc49896aab6cc1",
  "cid": "QmV1e64a3c6ee048e89286302a5b0c4f4742f6acde17",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285844,
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
      "evaluated_at": 1760285844
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
  "sig": "d9848da362682af663b22c401cfa717fd0ddaf1a190b0fe27bf69c461b42bc8a"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009595557022
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 4, 'first_seen': 1760285764, 'matching_hash': '3443c05f2ecc9733'}}}