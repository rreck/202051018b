```json
{
  "id": "40c3794f023eea8c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289529,
  "host_pid": "9e6742732c60:1",
  "hash": "a1624a0c70daadbc33ca86af3f6dec94c8324353764494b2f35db8f552f30f08",
  "cid": "QmV1a1624a0c70daadbc33ca86af3f6dec94c8324353",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289529,
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
      "evaluated_at": 1760289529
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
  "sig": "9cef3679dcfce8642861027952a05cb74cc95948d5d8d79782bc4badb3f0e9e1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460208894
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 126, 'threshold': 50, 'total_amount': 60585210, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760285763, 'matching_hash': '36d88bd4e0ec214b'}}}