```json
{
  "id": "5bcee839cd5cb441",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289662,
  "host_pid": "9e6742732c60:1",
  "hash": "294a2471cb7206a5918ea1a4c19fb6d3a8808129af40b2f7baecd92b43300ada",
  "cid": "QmV1294a2471cb7206a5918ea1a4c19fb6d3a8808129",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289662,
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
      "evaluated_at": 1760289662
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
  "sig": "66865fef21253865d23b3892efc7eb20bbf06cdcdeec68dcad1d1293b6ea1a45"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50, 'total_amount': 41053992, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}