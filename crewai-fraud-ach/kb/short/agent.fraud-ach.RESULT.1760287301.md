```json
{
  "id": "bb0f79323ac980c1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287301,
  "host_pid": "9e6742732c60:1",
  "hash": "5330061e7978b8cb3654d74307faea17840f9f81cad8476517d2bb1e5e7950ab",
  "cid": "QmV15330061e7978b8cb3654d74307faea17840f9f81",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287301,
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
      "evaluated_at": 1760287301
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
  "sig": "ce83b3b258411f50ddc6014f24b0c43bcc527ec91871951c877bfaf5fb5c1824"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201469103825
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 55, 'threshold': 50, 'total_amount': 19898395, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 54, 'first_seen': 1760285764, 'matching_hash': 'e83bf56ea8077a45'}}}