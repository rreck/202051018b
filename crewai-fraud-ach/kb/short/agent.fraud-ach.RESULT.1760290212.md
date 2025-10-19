```json
{
  "id": "4ea8e86dfc4ff570",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290212,
  "host_pid": "9e6742732c60:1",
  "hash": "7c3cb5773e27cc44afb12e1e9ddfaa2cf528e809a4c503a485bb3e830d84d99f",
  "cid": "QmV17c3cb5773e27cc44afb12e1e9ddfaa2cf528e809",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290212,
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
      "evaluated_at": 1760290212
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
  "sig": "acbebc47d6f02f510553206cd78d48ffbdcc3c26d5e0c53354b93799e4d00bd7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274578801
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 25292160, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285765, 'matching_hash': 'c58645b7bcecdbfd'}}}