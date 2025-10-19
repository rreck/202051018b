```json
{
  "id": "ac9eb5f78fd2dcc2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285997,
  "host_pid": "9e6742732c60:1",
  "hash": "d57c5dc00c52b2904c45560b7b2378b9b197074a800d63dc929a7dcaee81c16f",
  "cid": "QmV1d57c5dc00c52b2904c45560b7b2378b9b197074a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285997,
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
      "evaluated_at": 1760285997
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
  "sig": "c6806c89d3f011190f5040792b91ed358a423ab3834c5b65930b44b308d3ad13"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000023536829
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 10, 'first_seen': 1760285763, 'matching_hash': 'cf71240b8169078c'}}}