```json
{
  "id": "96911a73c5356af0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289784,
  "host_pid": "9e6742732c60:1",
  "hash": "5c8696b4eabc965981fbfee10def423ad0a20a4fcdcb1895c29b86c2609bc946",
  "cid": "QmV15c8696b4eabc965981fbfee10def423ad0a20a4f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289784,
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
      "evaluated_at": 1760289784
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
  "sig": "34b022549407039c89359fa98ab4f120045c54d557be7824a0060e0de9aa08c3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150546450
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50, 'total_amount': 61785682, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760285763, 'matching_hash': '173a3d8db8c10352'}}}