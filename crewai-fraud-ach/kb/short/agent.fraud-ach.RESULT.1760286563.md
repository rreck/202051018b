```json
{
  "id": "26652c24cc8a7a96",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286563,
  "host_pid": "9e6742732c60:1",
  "hash": "017aca4fce34e736d384fae8a5c7c1ba2a492064cb2b843500de662a7d06019a",
  "cid": "QmV1017aca4fce34e736d384fae8a5c7c1ba2a492064",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286563,
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
      "evaluated_at": 1760286563
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
  "sig": "130f16d0892699c83c6deeb0c3cb4da1a4656aff791bb838fd79d75e284c785f"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009598206386
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 28, 'first_seen': 1760285765, 'matching_hash': '83614fe1c845b0af'}}}