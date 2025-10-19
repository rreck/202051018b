```json
{
  "id": "6dd28b57e78564b6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285928,
  "host_pid": "9e6742732c60:1",
  "hash": "7dee02ca3dbc0bedfac33e512d418ed2845a882440ed6a547859fc03a979373a",
  "cid": "QmV17dee02ca3dbc0bedfac33e512d418ed2845a8824",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285928,
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
      "evaluated_at": 1760285928
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
  "sig": "3ae577110389d6c646a0210411621d97732768c3e3f9f18a313f522028e203fd"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 7, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}