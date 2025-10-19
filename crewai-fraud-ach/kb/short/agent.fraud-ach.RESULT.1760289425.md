```json
{
  "id": "96b0392e4fd89e66",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289425,
  "host_pid": "9e6742732c60:1",
  "hash": "8a1cdb5793bde22626fbfbcab621310126a7b527e34bc0eff149b6f18d3818e3",
  "cid": "QmV18a1cdb5793bde22626fbfbcab621310126a7b527",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289425,
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
      "evaluated_at": 1760289425
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
  "sig": "13f654a8eddb93bd0b627ac2dff6d944319b9f8ba44215ac80d6c27d3ec167a4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023218255
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 123, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 122, 'first_seen': 1760285763, 'matching_hash': '1151ecc015fd8f1a'}}}