```json
{
  "id": "b29dc881b9c61a5b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290551,
  "host_pid": "9e6742732c60:1",
  "hash": "a353b70ce88949fb9ad53dc031021bbfaefcf0348d91087ec3abbf52316a7b3f",
  "cid": "QmV1a353b70ce88949fb9ad53dc031021bbfaefcf034",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290551,
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
      "evaluated_at": 1760290551
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
  "sig": "0693bfcd6531c98d1c88e7f5f3ff24a34e51d53fdec789f321c672522c078b02"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034624068
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50, 'total_amount': 21918168, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285763, 'matching_hash': 'e9c21d379839efb6'}}}