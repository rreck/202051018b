```json
{
  "id": "4e3b6dc99c9a9ce3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289447,
  "host_pid": "9e6742732c60:1",
  "hash": "58e08c01cef848912100da73c659f81f4b5a1043feaa635dc23e805c403969db",
  "cid": "QmV158e08c01cef848912100da73c659f81f4b5a1043",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289447,
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
      "evaluated_at": 1760289447
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
  "sig": "697b74ead2a537e0018e454e7052ad32fbe663e6b0d21619215ea3cdee5cd377"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594086126
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 123, 'threshold': 50, 'total_amount': 16706721, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 122, 'first_seen': 1760285765, 'matching_hash': '58168677024efb84'}}}