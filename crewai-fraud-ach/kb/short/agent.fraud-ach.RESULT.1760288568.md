```json
{
  "id": "4f28f895ba5fb6f8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288568,
  "host_pid": "9e6742732c60:1",
  "hash": "4bf214d0e50b7c06824e22e9313c399f3e376529db44cb46c7c65263f18daeae",
  "cid": "QmV14bf214d0e50b7c06824e22e9313c399f3e376529",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288568,
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
      "evaluated_at": 1760288568
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
  "sig": "7734cd07c48ca2cc7b7cbb613905daccaa4cc6cf54aa0938eb0678f6ab9fca93"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463787734
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 97, 'threshold': 50, 'total_amount': 31166585, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 96, 'first_seen': 1760285764, 'matching_hash': 'c4d507dbbdae18b2'}}}