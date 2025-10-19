```json
{
  "id": "ea055446cd72803b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287385,
  "host_pid": "9e6742732c60:1",
  "hash": "f4ea51dc5f7102674fbcb1c280ccfc4ebd99787de96414099ca9d6ea5e8e2b33",
  "cid": "QmV1f4ea51dc5f7102674fbcb1c280ccfc4ebd99787d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287385,
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
      "evaluated_at": 1760287385
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
  "sig": "0b7d599c7afbd0fbcd0d1f00e01cdb1b3a001e01b51485baf8a336a5de03f568"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000025723119
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 58, 'threshold': 50, 'total_amount': 27351582, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 57, 'first_seen': 1760285764, 'matching_hash': '7f709c8256c8a242'}}}