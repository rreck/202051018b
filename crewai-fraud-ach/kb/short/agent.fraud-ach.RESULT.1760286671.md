```json
{
  "id": "9198043ea2752602",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286671,
  "host_pid": "9e6742732c60:1",
  "hash": "413e1221122754012795d2fc99524b426a96bb7b444aa37efb3070484b0ef9aa",
  "cid": "QmV1413e1221122754012795d2fc99524b426a96bb7b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286671,
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
      "evaluated_at": 1760286671
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
  "sig": "d5e9c2c913ccdd4943d1298af3eeba34dcb88af30f6273d15d0bfc2d66e3b914"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000245772760
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 32, 'first_seen': 1760285763, 'matching_hash': '6b0c370090b6c980'}}}