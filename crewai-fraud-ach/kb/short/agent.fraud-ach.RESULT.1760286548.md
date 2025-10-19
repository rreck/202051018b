```json
{
  "id": "55d2b39f39431e34",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286548,
  "host_pid": "9e6742732c60:1",
  "hash": "857828d4da69b601cb37c55e5e64077be02a6a8cc18dd8743f7b4756cb5409f2",
  "cid": "QmV1857828d4da69b601cb37c55e5e64077be02a6a8c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286548,
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
      "evaluated_at": 1760286548
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
  "sig": "eba3a0ab09ae0bb2ed24a84d23c9412dbe650227f081b97d0b62ef1c324bbd83"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009596892918
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 28, 'first_seen': 1760285763, 'matching_hash': 'c247331c92498799'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 28, 'first_seen': 1760285763, 'matching_hash': '152f3a2a027ae633'}}}