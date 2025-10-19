```json
{
  "id": "46cfaede65cb6d5d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289307,
  "host_pid": "9e6742732c60:1",
  "hash": "a7b47fe815afe81b00c91269402cd21619f6f8ab15c510aef1b9acc0417f136c",
  "cid": "QmV1a7b47fe815afe81b00c91269402cd21619f6f8ab",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289307,
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
      "evaluated_at": 1760289307
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
  "sig": "5a893bba421f669047fa82d9563f789f8822cd8f39dcf4c285d0202b21372d86"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158656793
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 119, 'threshold': 50, 'total_amount': 36068186, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 118, 'first_seen': 1760285765, 'matching_hash': 'b1ac6f9d66d66d2b'}}}