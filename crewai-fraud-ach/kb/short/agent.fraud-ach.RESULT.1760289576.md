```json
{
  "id": "0dabf3b58357cdcc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289576,
  "host_pid": "9e6742732c60:1",
  "hash": "f06043acc8a6fa1e166a8915478932623b1cd1d7786dce8e54a1cffa7b3b2425",
  "cid": "QmV1f06043acc8a6fa1e166a8915478932623b1cd1d7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289576,
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
      "evaluated_at": 1760289576
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
  "sig": "46b53c42b0e07be0af2a0bad2a693a6589ba55ef2ae5eaf228aa3e1d76fbc5da"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463621906
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 127, 'threshold': 50, 'total_amount': 42943272, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 126, 'first_seen': 1760285763, 'matching_hash': 'c1b23d91813533f7'}}}