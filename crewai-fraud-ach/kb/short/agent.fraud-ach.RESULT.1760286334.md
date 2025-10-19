```json
{
  "id": "283a83c3a57190b6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286334,
  "host_pid": "9e6742732c60:1",
  "hash": "8e57d4ffaa7507711c656a905809ce18b7a183192df96143912f9ce8ea6aa12c",
  "cid": "QmV18e57d4ffaa7507711c656a905809ce18b7a18319",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286334,
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
      "evaluated_at": 1760286334
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "2126b25a77a88f581d635e8e82ec3c9978b2b1ad7a6db22ea3944d0c594dc25a"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009591103574
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10291050, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 21, 'first_seen': 1760285763, 'matching_hash': 'b913753ac5280baa'}}}