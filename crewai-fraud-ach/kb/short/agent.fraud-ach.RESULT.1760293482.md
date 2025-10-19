```json
{
  "id": "e40e4b4788026c7f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293482,
  "host_pid": "9e6742732c60:1",
  "hash": "8de55774c89799fdef5b35e46f069b9b017ce83ea950eb2fa65e3c6daeb73890",
  "cid": "QmV18de55774c89799fdef5b35e46f069b9b017ce83e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293482,
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
      "evaluated_at": 1760293482
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
  "sig": "068d7a4c2ca44c2bc64b4b877e124e623cf9def747fbdc63b46c84881a2e8981"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155748621
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 101773899, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285764, 'matching_hash': 'df4db45348ec5c9a'}}}