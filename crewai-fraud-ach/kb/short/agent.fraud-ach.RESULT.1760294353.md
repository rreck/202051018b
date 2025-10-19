```json
{
  "id": "debd39a5a1644600",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294353,
  "host_pid": "9e6742732c60:1",
  "hash": "4f920192278e471be788e10e61fece8f48849724a907427b26053283c84e70a3",
  "cid": "QmV14f920192278e471be788e10e61fece8f48849724",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294353,
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
      "evaluated_at": 1760294353
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
  "sig": "190526a914e0bb08832080ceb09af5a06b1f8e2d1a656f80b2711dc74b5a7541"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462554282
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 13743224, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': '2083692f538c0312'}}}