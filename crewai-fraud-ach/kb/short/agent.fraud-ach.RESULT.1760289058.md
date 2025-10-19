```json
{
  "id": "2391a920f38c20f6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289058,
  "host_pid": "9e6742732c60:1",
  "hash": "f1c6ce78650c3ff577911ccbd059a512aff9b567b1f7ac2e31688b53912b30a6",
  "cid": "QmV1f1c6ce78650c3ff577911ccbd059a512aff9b567",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289058,
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
      "evaluated_at": 1760289058
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
  "sig": "89193a6c715b10d89ba2eeab6ce9af1913a741fa1cc8bc725be4f6d1b684058b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278037585
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 112, 'threshold': 50, 'total_amount': 11896192, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 111, 'first_seen': 1760285763, 'matching_hash': '27cb7a10328c75d5'}}}