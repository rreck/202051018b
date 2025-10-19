```json
{
  "id": "e00d731cc9f740af",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286345,
  "host_pid": "9e6742732c60:1",
  "hash": "05939ba36d7c55b3a37fdd7febd4641dc9dbdefc38b9ba3a28d2492dcc2c8f22",
  "cid": "QmV105939ba36d7c55b3a37fdd7febd4641dc9dbdefc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286345,
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
      "evaluated_at": 1760286345
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
  "sig": "6a483100baef155a7458586c8ae2565c337781a4b7dd700d0a09196ee9c0b1cb"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201460625527
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10563740, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 21, 'first_seen': 1760285765, 'matching_hash': 'd2e448c8360c8b26'}}}