```json
{
  "id": "ac0db4808078ace8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291886,
  "host_pid": "9e6742732c60:1",
  "hash": "f21ab169fe0839ba3e3f11d8c134e8d60b499daa969fc6aea31e6688c64a066c",
  "cid": "QmV1f21ab169fe0839ba3e3f11d8c134e8d60b499daa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291886,
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
      "evaluated_at": 1760291886
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
  "sig": "a5bfde067a0732563ef450e028aa57d8189fd0ba5800165f06ff2eae1ca84939"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034778259
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 33659640, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285763, 'matching_hash': 'b6b775805828fc60'}}}