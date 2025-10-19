```json
{
  "id": "85f240e119721428",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290387,
  "host_pid": "9e6742732c60:1",
  "hash": "aea4d0bdece0b07d8d440f96269070cbc9980b1a9d7000237be07414cbb3ba68",
  "cid": "QmV1aea4d0bdece0b07d8d440f96269070cbc9980b1a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290387,
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
      "evaluated_at": 1760290388
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
  "sig": "f5c0c1669cd74ed433f0223824f72a1546e5753643429c2e92a33ba819fc5a1d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000024349722
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285763, 'matching_hash': '3e275568f5204778'}}}