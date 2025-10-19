```json
{
  "id": "6ba1b1e3cbb75249",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289614,
  "host_pid": "9e6742732c60:1",
  "hash": "65ec73799346ed2c93d77a05c663b98d99c85e99e9bfcbbcafe076fb763c60f1",
  "cid": "QmV165ec73799346ed2c93d77a05c663b98d99c85e99",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289614,
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
      "evaluated_at": 1760289614
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
  "sig": "94a44b101efa680ebd369c30a9cd4b680dfe6180181abd20b1a4c671900ef1e1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039215537
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 128, 'threshold': 50, 'total_amount': 30923520, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 127, 'first_seen': 1760285765, 'matching_hash': '4decba5555bb1e33'}}}