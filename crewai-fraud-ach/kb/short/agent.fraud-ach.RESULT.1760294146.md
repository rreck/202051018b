```json
{
  "id": "e81da7b2889b8949",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294146,
  "host_pid": "9e6742732c60:1",
  "hash": "53a8c6226d34ec47dd2358d66f3c235257a7e60db5ad449f154cf8789406f76f",
  "cid": "QmV153a8c6226d34ec47dd2358d66f3c235257a7e60d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294146,
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
      "evaluated_at": 1760294146
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
  "sig": "420578c262fe267b5fe3ade5fc8f02811ed52d048cf8c7a05151627bd45f6ce6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245748791
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 46300704, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285765, 'matching_hash': 'b01b0e655b1e1c55'}}}