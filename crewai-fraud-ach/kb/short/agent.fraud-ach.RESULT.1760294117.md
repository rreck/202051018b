```json
{
  "id": "44c4ca1a9b6c5720",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294117,
  "host_pid": "9e6742732c60:1",
  "hash": "1908cae82b08901c6532553eae419e01c84c857b7e3ddeeaf714a5e7d1c238e2",
  "cid": "QmV11908cae82b08901c6532553eae419e01c84c857b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294117,
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
      "evaluated_at": 1760294117
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
  "sig": "4f6476ef55722044e7075e6af359d59358cc65e51ed2363d6950c1cfbb34cf94"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249225817
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 54647368, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285763, 'matching_hash': 'b4dc0a1cb279f16e'}}}