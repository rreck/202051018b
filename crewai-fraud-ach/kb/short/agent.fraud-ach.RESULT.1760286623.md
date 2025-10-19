```json
{
  "id": "b47a16718e90ca56",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286623,
  "host_pid": "9e6742732c60:1",
  "hash": "2615c0396acd53df09532923d68360893401f7413aa0b3106ba394ac236760ac",
  "cid": "QmV12615c0396acd53df09532923d68360893401f741",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286623,
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
      "evaluated_at": 1760286623
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
  "sig": "eb0fed1a370fb85bc9bb708d95d9bb954fe86ac6796cf6f5bcab7bf4446eaffe"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 30, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}