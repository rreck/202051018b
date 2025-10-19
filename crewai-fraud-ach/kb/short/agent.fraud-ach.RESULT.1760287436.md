```json
{
  "id": "e677236e8bbf855b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287436,
  "host_pid": "9e6742732c60:1",
  "hash": "fcfbd00b61edfe42269b604903850e580135b8a5b0fd14164d8e3d652f6b8d5e",
  "cid": "QmV1fcfbd00b61edfe42269b604903850e580135b8a5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287436,
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
      "evaluated_at": 1760287436
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
  "sig": "d75c03521d9fe5dc1fdb5439e3675267bba5b99ee06b195d7d593d2a558ddf41"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000244291071
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 60, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 59, 'first_seen': 1760285763, 'matching_hash': '1f8fb3dc368ee7c3'}}}een': 1760285763, 'matching_hash': '525a45536127a4d2'}}}