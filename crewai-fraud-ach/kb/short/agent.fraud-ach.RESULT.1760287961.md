```json
{
  "id": "74099346a2d3871d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287961,
  "host_pid": "9e6742732c60:1",
  "hash": "3da6f6cfebd6c244be1054865f4c71d6da999d2be645b4f5cac4920c44025d63",
  "cid": "QmV13da6f6cfebd6c244be1054865f4c71d6da999d2b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287961,
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
      "evaluated_at": 1760287961
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
  "sig": "0d5ba9237236ba526c1d85065a415e06a366c01a9ece34d192e034512ae69fb9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153425339
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 78, 'threshold': 50, 'total_amount': 34468356, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 77, 'first_seen': 1760285763, 'matching_hash': 'd6fcd27194bc1174'}}}