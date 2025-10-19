```json
{
  "id": "cb25c4cea2a7d9c4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289469,
  "host_pid": "9e6742732c60:1",
  "hash": "e7b286d3dc1d52435c899dd74a02076a68d34f262429d1e0eb233be57d6a7594",
  "cid": "QmV1e7b286d3dc1d52435c899dd74a02076a68d34f26",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289469,
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
      "evaluated_at": 1760289469
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
  "sig": "1fe1b76d0ea510c38d315bac42f9ce9480c89cc1969c8599153769523e04cb1e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594957329
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 124, 'threshold': 50, 'total_amount': 61726456, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 123, 'first_seen': 1760285763, 'matching_hash': '2b2bf7f9f831f062'}}}