```json
{
  "id": "682144f36ae14212",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286187,
  "host_pid": "9e6742732c60:1",
  "hash": "71569222f6ae9b82473aaace9e00b62c671e0546dbd6cd675727ac81907278b3",
  "cid": "QmV171569222f6ae9b82473aaace9e00b62c671e0546",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286187,
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
      "evaluated_at": 1760286187
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
  "sig": "0a8400a9043ae39ddb13742fe5c0a8024e89306f75ea1ab8dacf61c6b2c6a881"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009593077739
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 16, 'first_seen': 1760285763, 'matching_hash': 'dc5b0e0c6a053908'}}}