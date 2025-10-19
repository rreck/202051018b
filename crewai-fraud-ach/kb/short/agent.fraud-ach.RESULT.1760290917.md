```json
{
  "id": "043110476ece928d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290917,
  "host_pid": "9e6742732c60:1",
  "hash": "c358a84f66c1e468966401a2e52e9783e26752501b22bc0cb9cea51197fcfd13",
  "cid": "QmV1c358a84f66c1e468966401a2e52e9783e2675250",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290917,
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
      "evaluated_at": 1760290917
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
  "sig": "2c96a5891bbe41aeff893d0065e94a4512a9b10a5fe725c82aa423bcc0da0b18"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022307864
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 76268142, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285765, 'matching_hash': '183a325d3d521c29'}}}