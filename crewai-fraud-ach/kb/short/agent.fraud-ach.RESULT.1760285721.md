```json
{
  "id": "a27dda8296a15280",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285721,
  "host_pid": "9e6742732c60:1",
  "hash": "6da4719178a632bc78f0607b61de1a3cbab369c3a3fde3c85d51bd014104fce7",
  "cid": "QmV16da4719178a632bc78f0607b61de1a3cbab369c3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285721,
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
      "evaluated_at": 1760285721
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
  "sig": "abe814a4e01c06f1b4a519bb476a3a8eb99036a2d501f02ace23cd7b79fe5753"
}
```

Fraud detected: duplicate_transaction (score: 90)
Transaction: 031201465682795
Details: {'velocity': {'fraud_detected': True, 'risk_score': 96, 'details': {'transaction_count': 73, 'threshold': 50, 'total_amount': 18389795, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 72, 'first_seen': 1760284979, 'matching_hash': 'c9bd5d9b74477b1c'}}}