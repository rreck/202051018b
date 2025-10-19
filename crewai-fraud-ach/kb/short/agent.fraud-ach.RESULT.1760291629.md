```json
{
  "id": "5b5876fe404e831e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291629,
  "host_pid": "9e6742732c60:1",
  "hash": "d0e0b9f7a00c70c304fd0f4d8d52c3f077bf710c10135408d9825f2f692bbf93",
  "cid": "QmV1d0e0b9f7a00c70c304fd0f4d8d52c3f077bf710c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291629,
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
      "evaluated_at": 1760291629
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
  "sig": "e7eb5104c09a3047dd375cd813f767751247410f1ad8a836da55c65c9f5d3971"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245911336
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 89103694, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285765, 'matching_hash': '6e0081c3975eda61'}}}