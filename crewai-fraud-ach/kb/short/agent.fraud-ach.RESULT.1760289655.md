```json
{
  "id": "7a65b82ac411db93",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289655,
  "host_pid": "9e6742732c60:1",
  "hash": "83a76023584425e3ef110d2696d12b948596fe7f6ebeedfa8a916ed1f904a9e2",
  "cid": "QmV183a76023584425e3ef110d2696d12b948596fe7f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289655,
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
      "evaluated_at": 1760289655
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
  "sig": "8a996a9dabf3a05ee67c98606280276586d0fad4c209a04fd54aba82682cf796"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032270621
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50, 'total_amount': 29763912, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760285764, 'matching_hash': '380f2fccd8369f51'}}}