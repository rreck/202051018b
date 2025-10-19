```json
{
  "id": "259f52108f20f868",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290361,
  "host_pid": "9e6742732c60:1",
  "hash": "718351776148faa7c615c7e27122eb3c990e8ae2d0ae1f5aa011d4dde3b6dd00",
  "cid": "QmV1718351776148faa7c615c7e27122eb3c990e8ae2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290361,
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
      "evaluated_at": 1760290361
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
  "sig": "4e7e1ba1ca3b3dd3b596cbde4882c5d674b0eb02ace4e200716dbea21d86e947"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025121499
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 18827524, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285763, 'matching_hash': 'a696ea0f650f1de2'}}}