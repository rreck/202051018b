```json
{
  "id": "2c4f2f7db0ea3a68",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286364,
  "host_pid": "9e6742732c60:1",
  "hash": "3ad355793492d3c18e0649a5bd9b141e331d4e0f0743b4e2a0ab145ab5f017dd",
  "cid": "QmV13ad355793492d3c18e0649a5bd9b141e331d4e0f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286364,
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
      "evaluated_at": 1760286364
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
  "sig": "fbbee7942dc78147dee1bb70d2f3dd661d6846e1b97d52b6a73353945e7472fc"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000240263900
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 22, 'first_seen': 1760285764, 'matching_hash': 'e5d68d31887f65d4'}}}