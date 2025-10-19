```json
{
  "id": "3306840494af4554",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289541,
  "host_pid": "9e6742732c60:1",
  "hash": "065a63732ff6792651940fb63f651802a9aa3a4da18d27e392c4689a50f165b6",
  "cid": "QmV1065a63732ff6792651940fb63f651802a9aa3a4d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289541,
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
      "evaluated_at": 1760289541
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
  "sig": "f4dd802d5a98555dccfcee7311d235ec9181913e705c7c428ceb63d09313e57b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277495051
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 126, 'threshold': 50, 'total_amount': 61353558, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760285763, 'matching_hash': 'b54d2b84a0558fd6'}}}