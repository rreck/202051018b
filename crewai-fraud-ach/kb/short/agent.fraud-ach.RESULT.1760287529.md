```json
{
  "id": "680850784926d508",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287529,
  "host_pid": "9e6742732c60:1",
  "hash": "2de85162e914c9dd30de3277be9884969650faffb5d03bf8db40c04aff852477",
  "cid": "QmV12de85162e914c9dd30de3277be9884969650faff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287529,
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
      "evaluated_at": 1760287529
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
  "sig": "e957e2ecbe7d7e8a3335411d7caf0ffc68c767a038044e791215ebc86bf7ecf8"
}
```

Fraud detected: duplicate_transaction (score: 80)
Transaction: 121000244752813
Details: {'velocity': {'fraud_detected': True, 'risk_score': 76, 'details': {'transaction_count': 63, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 62, 'first_seen': 1760285765, 'matching_hash': 'eddee7b4753d10e9'}}}