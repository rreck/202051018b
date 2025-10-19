```json
{
  "id": "c6acca9b0219a969",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292945,
  "host_pid": "9e6742732c60:1",
  "hash": "49b30a65dcf4eaa82d242dad4bbd7bc8dcfc5553719bd43ff0dba5f5330d7511",
  "cid": "QmV149b30a65dcf4eaa82d242dad4bbd7bc8dcfc5553",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292945,
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
      "evaluated_at": 1760292945
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
  "sig": "5ea4eea13ce7a474081afd86ca83abdb8c21d0020b9139a9590b314482fe9265"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245329334
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 76706656, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285765, 'matching_hash': 'de3fbc58a94e529a'}}}nd_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}