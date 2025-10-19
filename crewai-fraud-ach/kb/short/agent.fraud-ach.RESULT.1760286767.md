```json
{
  "id": "79f45f3e650bef07",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286767,
  "host_pid": "9e6742732c60:1",
  "hash": "f92de0fcc5caa271710cdeda8bdfdb86ad0283e33b0fde2a221d48d0df01f012",
  "cid": "QmV1f92de0fcc5caa271710cdeda8bdfdb86ad0283e3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286767,
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
      "evaluated_at": 1760286767
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
  "sig": "5cc688d234cd2bfd03d68d1f792d51bf0a724a3ec10b930e122bff2a500eca47"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100270650471
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 35, 'first_seen': 1760285765, 'matching_hash': '471e898b7e147a60'}}}