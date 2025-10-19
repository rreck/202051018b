```json
{
  "id": "f695ac03be112144",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291923,
  "host_pid": "9e6742732c60:1",
  "hash": "4d59488071669a57078f3372ee09c9ee55c9eaa2148ebaba8eede7f2398757b3",
  "cid": "QmV14d59488071669a57078f3372ee09c9ee55c9eaa2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291923,
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
      "evaluated_at": 1760291923
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
  "sig": "635c87919d7c2182e480e51af7ff174a1950d54c8bf77d3f22fc32419db5d33e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594081907
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 92173044, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285763, 'matching_hash': 'b8f6a044d6b1da81'}}}