```json
{
  "id": "78df763d556452bf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286106,
  "host_pid": "9e6742732c60:1",
  "hash": "e64dff13a6ab0e02fd60998347f14653f0812a1924dcd659f877dc3322bcfe68",
  "cid": "QmV1e64dff13a6ab0e02fd60998347f14653f0812a19",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286106,
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
      "evaluated_at": 1760286106
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
  "sig": "56fc7133b9449b1bb4646d614961f327d9d816f10668c3e6bb0bd4b986d05b8f"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 13, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}