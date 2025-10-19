```json
{
  "id": "267762d4dc51fcc0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292837,
  "host_pid": "9e6742732c60:1",
  "hash": "d0e70c0ef2bb32f2faf84fbf75480ef3bd570a4ecf8555a2a1d6869f39005e85",
  "cid": "QmV1d0e70c0ef2bb32f2faf84fbf75480ef3bd570a4e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292837,
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
      "evaluated_at": 1760292837
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
  "sig": "579bce84bd088deab0dfab027dbe2cf5b6ff64c4220d09673df14ca079e504f7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156622392
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 49531464, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285763, 'matching_hash': '760602768636d516'}}}