```json
{
  "id": "d2d93c4ab3e798ae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286394,
  "host_pid": "9e6742732c60:1",
  "hash": "d4c5e841dc90430d7658ac43945742a01e0336bd2c0100e7e05544d75b073105",
  "cid": "QmV1d4c5e841dc90430d7658ac43945742a01e0336bd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286394,
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
      "evaluated_at": 1760286394
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
  "sig": "f22b9c2d9366ccebfb0dfc3d148cc1b5920c1715ae60d6b4af253d1aead32b55"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201464999191
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 23, 'first_seen': 1760285763, 'matching_hash': '0f07ea7feb264441'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 23, 'first_seen': 1760285763, 'matching_hash': 'b30e2736c805251a'}}}