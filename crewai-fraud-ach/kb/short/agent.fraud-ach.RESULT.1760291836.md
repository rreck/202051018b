```json
{
  "id": "4733a9723dea623f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291836,
  "host_pid": "9e6742732c60:1",
  "hash": "63cb215d6977676cf8516bec123fd67dc45c5285239d361fe63c659f440f83e1",
  "cid": "QmV163cb215d6977676cf8516bec123fd67dc45c5285",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291836,
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
      "evaluated_at": 1760291836
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
  "sig": "ce797680ad408bcd3fdfff78339d00f6040be1bc8d5314c4f84a8362a1b63f28"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590785424
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 12464712, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285763, 'matching_hash': 'b02577e012abfee0'}}}