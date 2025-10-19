```json
{
  "id": "b8d8e17e575d259a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291604,
  "host_pid": "9e6742732c60:1",
  "hash": "417083627a8ea478d84e6e903c447ca0afb17b2425029650cc090e3b5e7dd22a",
  "cid": "QmV1417083627a8ea478d84e6e903c447ca0afb17b24",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291604,
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
      "evaluated_at": 1760291604
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
  "sig": "fe2b7d139f420e4d1ad1c1b9bbd2fad0e6031fa0d771fa48a5e48a18559f0deb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029518652
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 13612950, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285763, 'matching_hash': 'e772ab4f6c2a0903'}}}