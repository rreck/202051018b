```json
{
  "id": "06461723f1158d2a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292550,
  "host_pid": "9e6742732c60:1",
  "hash": "a278c2bb1d39b30b19c15d9c5ab6b0bc20b31e816dd561c37c99aefcbc7632db",
  "cid": "QmV1a278c2bb1d39b30b19c15d9c5ab6b0bc20b31e81",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292550,
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
      "evaluated_at": 1760292550
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
  "sig": "79d394694c0e27b2aee02dacf6b73d8e36e42a00a25485411f6e50c9512075d0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021988031
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 50573400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285764, 'matching_hash': '88465ad333807d91'}}}