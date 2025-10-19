```json
{
  "id": "0584f0f61e705377",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289831,
  "host_pid": "9e6742732c60:1",
  "hash": "21e6ea865c36699cd52a059657da11da2cc6cbc676aaef619193b5ad9d38e775",
  "cid": "QmV121e6ea865c36699cd52a059657da11da2cc6cbc6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289831,
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
      "evaluated_at": 1760289831
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
  "sig": "2d1ed80662000fe9c6eb4b466a339c6cbd633387b9f10ee95f9d44e582187006"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157447901
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50, 'total_amount': 18119346, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285765, 'matching_hash': '08b33f5611b85fcf'}}}