```json
{
  "id": "9b754eafeddb7f4c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289470,
  "host_pid": "9e6742732c60:1",
  "hash": "243f27b0457c03df24fcab44a0d37c59aaa958ceb90f962107690ab961e180df",
  "cid": "QmV1243f27b0457c03df24fcab44a0d37c59aaa958ce",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289470,
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
      "evaluated_at": 1760289470
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
  "sig": "5d5af9d9e475b9f24db0babec08a2a73e4934a0752c6626bead5bc87cb265a74"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465949521
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 124, 'threshold': 50, 'total_amount': 48350080, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 123, 'first_seen': 1760285763, 'matching_hash': '5db5b45722d53397'}}}