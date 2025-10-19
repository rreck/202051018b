```json
{
  "id": "1e5855757a71bf48",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287069,
  "host_pid": "9e6742732c60:1",
  "hash": "f9ad09de49a14e93e6cd4a17add1e9eca11aa175975da4c8718934b9723d99e3",
  "cid": "QmV1f9ad09de49a14e93e6cd4a17add1e9eca11aa175",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287069,
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
      "evaluated_at": 1760287069
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
  "sig": "90964d6afac916c3c053908f017a8f8febfb61d01a670daf5e443f9116c1097b"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009594957329
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 23396318, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 46, 'first_seen': 1760285763, 'matching_hash': '2b2bf7f9f831f062'}}}g number checksum'}}}