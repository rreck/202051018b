```json
{
  "id": "ecb726032c99fba4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291400,
  "host_pid": "9e6742732c60:1",
  "hash": "105a1d4592ab531d6a59e2f598a701d2f12943d778491ec7c7425e7016e79cd7",
  "cid": "QmV1105a1d4592ab531d6a59e2f598a701d2f12943d7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291400,
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
      "evaluated_at": 1760291400
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
  "sig": "ae4ba8401c818dd9d4fd10da9dad8a3451bff6c65c636f7bab99f27d20393d78"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156622392
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 41837256, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285763, 'matching_hash': '760602768636d516'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '691661790', 'validation_error': 'Invalid routing number checksum'}}}