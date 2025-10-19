```json
{
  "id": "e7e9f5be3b07d080",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286819,
  "host_pid": "9e6742732c60:1",
  "hash": "e16f2e9216bbd12aa8f9760dc04f0bbaa4df08b0d51e1c501b636e34108d5e39",
  "cid": "QmV1e16f2e9216bbd12aa8f9760dc04f0bbaa4df08b0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286819,
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
      "evaluated_at": 1760286819
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "083281f3629accad8c032b8bae7b9db3b9dc9a66c2f16444103cb94f53cf7b87"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105159904059
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 17057744, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 37, 'first_seen': 1760285764, 'matching_hash': '7ad1725ffd2dadfd'}}}