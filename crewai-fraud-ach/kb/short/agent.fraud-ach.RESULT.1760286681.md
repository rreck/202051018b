```json
{
  "id": "af3aef910033ac55",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286681,
  "host_pid": "9e6742732c60:1",
  "hash": "fd44fc213a8808c5e0b6b0c454cd0fb762d0427079c19b71d96fd3b93fc09fcd",
  "cid": "QmV1fd44fc213a8808c5e0b6b0c454cd0fb762d04270",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286681,
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
      "evaluated_at": 1760286681
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
  "sig": "464ecdafdcab2b793f86e10c0a42f6e492861fcd5a4f1737825a298dfa18fc60"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000029386599
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 32, 'first_seen': 1760285765, 'matching_hash': 'b64c8fcbcd38380f'}}}