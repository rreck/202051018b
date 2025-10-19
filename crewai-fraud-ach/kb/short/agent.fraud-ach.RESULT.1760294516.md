```json
{
  "id": "134b6cae3e237e32",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294516,
  "host_pid": "9e6742732c60:1",
  "hash": "285155738f3c7c4889b9719821f9ed83a39cadadfd6c2d5d3564d80dbae046fa",
  "cid": "QmV1285155738f3c7c4889b9719821f9ed83a39cadad",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294516,
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
      "evaluated_at": 1760294516
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
  "sig": "c2bfca5a86aa4c5ec07e06fbdde2b8bbc62fc300085516709c4a3b331417bf1c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154024479
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 76217339, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285765, 'matching_hash': 'af946edf21c4a5d6'}}}