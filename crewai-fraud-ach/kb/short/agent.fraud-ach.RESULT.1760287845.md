```json
{
  "id": "ef52faf69dc597bb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287845,
  "host_pid": "9e6742732c60:1",
  "hash": "7b5b4d57419ef546199895c674cd04bfe3b2a72bc545c055f13cb9e8cabcf176",
  "cid": "QmV17b5b4d57419ef546199895c674cd04bfe3b2a72b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287845,
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
      "evaluated_at": 1760287845
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
  "sig": "315f480ae68f1dd004b0ab31d9b3d395ee5fbfcb75e7510b60261bb7e81be516"
}
```

Fraud detected: duplicate_transaction (score: 91)
Transaction: 031201467134805
Details: {'velocity': {'fraud_detected': True, 'risk_score': 98, 'details': {'transaction_count': 74, 'threshold': 50, 'total_amount': 20131330, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 73, 'first_seen': 1760285763, 'matching_hash': 'bc3c56d4b0e7489d'}}}