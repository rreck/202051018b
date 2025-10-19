```json
{
  "id": "d5640bd761abf29a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286179,
  "host_pid": "9e6742732c60:1",
  "hash": "989ed8672325fa06334df7dd676039f3aacbdc1fd725d1e3371bc7b19f461dde",
  "cid": "QmV1989ed8672325fa06334df7dd676039f3aacbdc1f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286179,
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
      "evaluated_at": 1760286179
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
  "sig": "be4b8f7411102458d091a52770d7b88f30bb45c64adfc41d7232b846730fe782"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000248193290
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 16, 'first_seen': 1760285763, 'matching_hash': '8925647bbeca80db'}}}