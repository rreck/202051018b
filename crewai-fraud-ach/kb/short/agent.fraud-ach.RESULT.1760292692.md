```json
{
  "id": "b58899c4f949d682",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292692,
  "host_pid": "9e6742732c60:1",
  "hash": "2ec94ad57a8bc97d2bc0dbbaadc5e9d0c26212e665cd3f16fb76f5446b85e52c",
  "cid": "QmV12ec94ad57a8bc97d2bc0dbbaadc5e9d0c26212e6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292692,
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
      "evaluated_at": 1760292692
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
  "sig": "92be0faa0bb97b8dcf916a3f4fc42ec8ecd350eb238b5b71c47cfbc871decd30"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000024349722
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 13200481, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285763, 'matching_hash': '3e275568f5204778'}}}