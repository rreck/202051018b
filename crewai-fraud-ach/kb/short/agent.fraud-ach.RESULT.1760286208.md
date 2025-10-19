```json
{
  "id": "42303997081bf9eb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286208,
  "host_pid": "9e6742732c60:1",
  "hash": "ff6c158a85d2483578569f3e843cb47435ca254343d761ebe3dca63b49d70670",
  "cid": "QmV1ff6c158a85d2483578569f3e843cb47435ca2543",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286208,
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
      "evaluated_at": 1760286208
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
  "sig": "a51a607929bdff6e6cb3de216694d3d795aeca66536301406495d0e7d6604376"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000029709484
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760285763, 'matching_hash': 'f2d4d1f000649e92'}}}