```json
{
  "id": "cbc3699a823a0c3f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285914,
  "host_pid": "9e6742732c60:1",
  "hash": "7380ed5a22dd247e1d5bf94b5834f1e0c9e8f9f4d4d27e51a5c1ae1699eb6fbe",
  "cid": "QmV17380ed5a22dd247e1d5bf94b5834f1e0c9e8f9f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285914,
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
      "evaluated_at": 1760285914
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
  "sig": "bc56846afc442bf1163c996fce470fc87cb5b97afaeb17f7d07e16311188960f"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201462772191
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 7, 'first_seen': 1760285763, 'matching_hash': '3cc4f4a3442921e3'}}}