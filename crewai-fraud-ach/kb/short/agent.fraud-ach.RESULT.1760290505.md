```json
{
  "id": "8ea0ffdd03efd611",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290505,
  "host_pid": "9e6742732c60:1",
  "hash": "205d42996280b0b0d2c43b8b38702b3b56c03692272aea9c9fb4512ed6a2c35b",
  "cid": "QmV1205d42996280b0b0d2c43b8b38702b3b56c03692",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290505,
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
      "evaluated_at": 1760290505
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
  "sig": "0fdad1fc8151e46a852cb56e8ea6670a6f1be3250ede1b5ebf40725b6a68567a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271137444
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 34444112, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285763, 'matching_hash': 'cc450f1d426424de'}}}