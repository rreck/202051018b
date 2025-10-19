```json
{
  "id": "07326bc9393b6763",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287126,
  "host_pid": "9e6742732c60:1",
  "hash": "e10ebd6f6138ee603f589c9788e9c415ae6931a0f860b45867e2da4a51349024",
  "cid": "QmV1e10ebd6f6138ee603f589c9788e9c415ae6931a0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287126,
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
      "evaluated_at": 1760287126
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
  "sig": "3fd57d4e425593fcdcb4d841386046482477202fe73cb37144537102640e78ee"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000029384681
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 48, 'first_seen': 1760285764, 'matching_hash': '45a3ccbce684d395'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 48, 'first_seen': 1760285763, 'matching_hash': '4e5cfda15432477b'}}}