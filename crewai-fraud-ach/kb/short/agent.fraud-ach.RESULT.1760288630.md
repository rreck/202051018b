```json
{
  "id": "a7f24d86faa300cb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288630,
  "host_pid": "9e6742732c60:1",
  "hash": "0028fec7b83b2b5ebc5f030624213001511112fd8bab052b9b694d72e0466940",
  "cid": "QmV10028fec7b83b2b5ebc5f030624213001511112fd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288630,
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
      "evaluated_at": 1760288630
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
  "sig": "5c2121eba84cb0147711a0d2cbee834cea22af51c81443b65ab7eb862f1c91bb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028860438
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 99, 'threshold': 50, 'total_amount': 29057292, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 98, 'first_seen': 1760285763, 'matching_hash': '1ce58b471eab5597'}}}