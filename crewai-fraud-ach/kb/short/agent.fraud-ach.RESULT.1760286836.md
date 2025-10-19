```json
{
  "id": "7a2733b605ab9372",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286836,
  "host_pid": "9e6742732c60:1",
  "hash": "48416e7a36c6cd486b5609b910f02bb79ec0db66ccc9949eb0fc6721e773942c",
  "cid": "QmV148416e7a36c6cd486b5609b910f02bb79ec0db66",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286836,
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
      "evaluated_at": 1760286836
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
  "sig": "d7045b7592ee3090cd80de33649dd627ed5f8fb50bd26dfbdd0fce451bcd7364"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009593402675
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 38, 'first_seen': 1760285763, 'matching_hash': '1478dad6bc2a5e7e'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 38, 'first_seen': 1760285763, 'matching_hash': '1ef68d78d8cabe5b'}}}