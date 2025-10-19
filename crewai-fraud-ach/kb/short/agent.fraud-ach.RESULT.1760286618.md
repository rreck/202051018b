```json
{
  "id": "7002ee49f1d077ff",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286618,
  "host_pid": "9e6742732c60:1",
  "hash": "1aedce19509f57d503c953c981f97ec17187f9343f14c989d1097c1f90377b49",
  "cid": "QmV11aedce19509f57d503c953c981f97ec17187f934",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286618,
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
      "evaluated_at": 1760286618
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
  "sig": "86ef04d578cc694ca03f87a5028615c48126be461b6e0199666d8766f4067b9a"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000031078531
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 30, 'first_seen': 1760285765, 'matching_hash': '2bea5b783a868e31'}}}