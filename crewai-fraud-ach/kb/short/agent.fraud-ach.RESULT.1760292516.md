```json
{
  "id": "a0b3a685fe0d32e1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292516,
  "host_pid": "9e6742732c60:1",
  "hash": "0dbbfde6465e078614ecdc7321aa11fde3de54b74824f68c9949749c28507a20",
  "cid": "QmV10dbbfde6465e078614ecdc7321aa11fde3de54b7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292516,
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
      "evaluated_at": 1760292516
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
  "sig": "5b3a98631213990af046caac60c7232e5583039cf6c08e99cfc6e1d47a837069"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034624068
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 28507944, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285763, 'matching_hash': 'e9c21d379839efb6'}}}