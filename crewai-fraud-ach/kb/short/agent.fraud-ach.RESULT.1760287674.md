```json
{
  "id": "adc996b52623c5fa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287674,
  "host_pid": "9e6742732c60:1",
  "hash": "58d4fcc7d408e8a9904019a39eaef3698875bb66b0b182fda0bdfe157ec977c5",
  "cid": "QmV158d4fcc7d408e8a9904019a39eaef3698875bb66",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287674,
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
      "evaluated_at": 1760287674
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
  "sig": "ec408433c7ab87dabbea3c4187df889f7b75112a5a2bb9671ac6be680ddeb47c"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100270650471
Details: {'velocity': {'fraud_detected': True, 'risk_score': 86, 'details': {'transaction_count': 68, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 67, 'first_seen': 1760285765, 'matching_hash': '471e898b7e147a60'}}}