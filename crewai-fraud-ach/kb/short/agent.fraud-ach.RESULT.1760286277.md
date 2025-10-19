```json
{
  "id": "c87dd9abbc3b7068",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286277,
  "host_pid": "9e6742732c60:1",
  "hash": "8ab7f4b889dd062d93dfbfceb744a142f2b25e0b1ce3c99afbcb3ee19ca28088",
  "cid": "QmV18ab7f4b889dd062d93dfbfceb744a142f2b25e0b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286277,
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
      "evaluated_at": 1760286277
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
  "sig": "a32aee93721fc13f2daf8497fe3ae57952f3b0310e2eab74e89fb27e5aa2c6c7"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000034981344
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 19, 'first_seen': 1760285765, 'matching_hash': '0030d58ae3a464b4'}}}