```json
{
  "id": "b7ab910d5bab11dc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286242,
  "host_pid": "9e6742732c60:1",
  "hash": "ad96550fa2e9151d288443e12994c653a1e05671b70c39e4305522b2ed5238f1",
  "cid": "QmV1ad96550fa2e9151d288443e12994c653a1e05671",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286242,
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
      "evaluated_at": 1760286242
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
  "sig": "a6889f61dca06c43f887f297da8835d11c2011ee1dd22b434ea67632b68e28e1"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009592426992
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 18, 'first_seen': 1760285763, 'matching_hash': '6c96fa15a49bffda'}}}