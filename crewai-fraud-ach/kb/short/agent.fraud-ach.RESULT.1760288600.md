```json
{
  "id": "92af6ccd1b0bafb6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288600,
  "host_pid": "9e6742732c60:1",
  "hash": "9cd1b3b806c13390e67052a114072bdef84d4b790c266d6bef81c0949c4664c2",
  "cid": "QmV19cd1b3b806c13390e67052a114072bdef84d4b79",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288600,
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
      "evaluated_at": 1760288600
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
  "sig": "e8997078cb345e31cda5e205e373489f743f35cb97e2cac775b8f3cf809384c6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240953214
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 98, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 97, 'first_seen': 1760285764, 'matching_hash': 'cfdb33c4cfd6ba9b'}}}