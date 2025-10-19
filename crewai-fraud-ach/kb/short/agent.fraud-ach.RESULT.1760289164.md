```json
{
  "id": "89b36dd9586879db",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289164,
  "host_pid": "9e6742732c60:1",
  "hash": "aa515913104ca7ebe6f04b83dc6e2a89578db712aec95257886c9ab57fe012cf",
  "cid": "QmV1aa515913104ca7ebe6f04b83dc6e2a89578db712",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289164,
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
      "evaluated_at": 1760289164
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
  "sig": "77e57b0f786ddd9d74b4ac35973893e8437295989c9c10b1f05b69ae39abfbe9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156494107
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 115, 'threshold': 50, 'total_amount': 57393855, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 114, 'first_seen': 1760285764, 'matching_hash': 'c1327b457e76afdd'}}}