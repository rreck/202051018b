```json
{
  "id": "aa8e2491c0e708d8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289223,
  "host_pid": "9e6742732c60:1",
  "hash": "1b9f33baf9749c8bb5ff0c6673096bfa515b4433c896fa6cee5fb923fb7937a6",
  "cid": "QmV11b9f33baf9749c8bb5ff0c6673096bfa515b4433",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289223,
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
      "evaluated_at": 1760289223
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
  "sig": "e611248e43ee6e590230a5d8952515655d569a7b8c67e10807a43da3b2b4f427"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156622392
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 117, 'threshold': 50, 'total_amount': 28131948, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 116, 'first_seen': 1760285763, 'matching_hash': '760602768636d516'}}}