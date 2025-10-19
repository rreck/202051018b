```json
{
  "id": "e5bd4fa8b9645a39",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287280,
  "host_pid": "9e6742732c60:1",
  "hash": "c824154067500269c7c77c3121ab4086699ed3fee6e64716283cefc661b51b41",
  "cid": "QmV1c824154067500269c7c77c3121ab4086699ed3fe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287280,
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
      "evaluated_at": 1760287280
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
  "sig": "8a27baa779c319bee6800cebc2baf9520398936a3803101caa332d5173774c51"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 54, 'threshold': 50, 'total_amount': 17185392, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 53, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}