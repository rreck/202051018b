```json
{
  "id": "0e85c9714a09bf01",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288218,
  "host_pid": "9e6742732c60:1",
  "hash": "28aa6cac85c9a2f63e2fede8e0aa7fcb08b39dd9d1ea8344b1c5b696d78aaa44",
  "cid": "QmV128aa6cac85c9a2f63e2fede8e0aa7fcb08b39dd9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288218,
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
      "evaluated_at": 1760288218
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
  "sig": "29c18fb5b8201e6029aa85b2d28bd99e322fc1c2516e54e9f12a77680613f0fd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249867755
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 86, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 85, 'first_seen': 1760285765, 'matching_hash': '3e6b26eb59ce898a'}}}