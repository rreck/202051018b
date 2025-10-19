```json
{
  "id": "8fc5e4688db65472",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292569,
  "host_pid": "9e6742732c60:1",
  "hash": "161a1e8bfad7e3addba024e7a2877fd4539b234341c37eed51a304d3ae854c8e",
  "cid": "QmV1161a1e8bfad7e3addba024e7a2877fd4539b2343",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292569,
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
      "evaluated_at": 1760292569
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
  "sig": "3e7f908a282eb969731ade3e59d1f5a96b596fb846e6cae62e5083e4b4182b67"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464170386
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 16333800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285764, 'matching_hash': 'cc3f2cd033134006'}}}