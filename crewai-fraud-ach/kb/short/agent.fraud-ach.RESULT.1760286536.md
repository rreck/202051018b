```json
{
  "id": "3150f26d15aefe6e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286536,
  "host_pid": "9e6742732c60:1",
  "hash": "47ea9ca7b21f9f76946de25affedd62a190170486b0df12d02b08e6ccc7f2286",
  "cid": "QmV147ea9ca7b21f9f76946de25affedd62a19017048",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286536,
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
      "evaluated_at": 1760286536
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
  "sig": "0996e5e5a9a106d9a66570ae60585d995fcfdeb8bd5764842bc479e996ffc3ce"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 27, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}