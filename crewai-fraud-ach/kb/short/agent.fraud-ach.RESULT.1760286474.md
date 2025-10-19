```json
{
  "id": "54a98742c4804101",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286474,
  "host_pid": "9e6742732c60:1",
  "hash": "b7b3b581b07a430a3eb6ff4baa6a12548fe6d1b78e5f3868fd4d8b782c7b3a3a",
  "cid": "QmV1b7b3b581b07a430a3eb6ff4baa6a12548fe6d1b7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286474,
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
      "evaluated_at": 1760286474
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
  "sig": "e932bb39feef83e082645017667abc25c9afeae2cecbcf3c44615e2e5713c050"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105158642736
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 25, 'first_seen': 1760285765, 'matching_hash': '1f64147e0a165b3c'}}}