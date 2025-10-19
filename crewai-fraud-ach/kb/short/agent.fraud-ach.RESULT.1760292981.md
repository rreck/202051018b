```json
{
  "id": "7db8689bee79ebf0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292981,
  "host_pid": "9e6742732c60:1",
  "hash": "ed673f28a45523cee1b56404f10c9a2db6816734177d9813f5f5455dd2aadc06",
  "cid": "QmV1ed673f28a45523cee1b56404f10c9a2db6816734",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292981,
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
      "evaluated_at": 1760292981
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
  "sig": "bc2a5e0fc823eb842c8e8183bd747eef37c33b99ea18c5b252c33cc9dec9cb1b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272056474
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 10909591, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285763, 'matching_hash': 'eb54a2a49d3a706d'}}}