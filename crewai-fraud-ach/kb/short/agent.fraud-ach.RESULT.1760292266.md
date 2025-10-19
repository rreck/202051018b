```json
{
  "id": "80e21f681705d136",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292266,
  "host_pid": "9e6742732c60:1",
  "hash": "44cca879b7643316f9e2e2b43853cc23d6d84b061b7e8bc782b5923121d7f6f8",
  "cid": "QmV144cca879b7643316f9e2e2b43853cc23d6d84b06",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292266,
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
      "evaluated_at": 1760292266
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
  "sig": "d8727ebb5b1700749cd0b77e0c75f3c046512eec734ad04320be094a72e67f0f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270864889
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 36881146, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285763, 'matching_hash': 'c03eacc7eaf45e0d'}}}