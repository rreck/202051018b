```json
{
  "id": "d80815cfba1f23a4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290054,
  "host_pid": "9e6742732c60:1",
  "hash": "28e6ef9b101220b15a7f8b0e2eac50383020a015e99ea4bdaf98945f3e4da0fd",
  "cid": "QmV128e6ef9b101220b15a7f8b0e2eac50383020a015",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290054,
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
      "evaluated_at": 1760290054
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
  "sig": "cb8b18c92e4093c11b2e66caff6c426d99dfabcb91665a71c7588dcbe737430d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245772760
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285763, 'matching_hash': '6b0c370090b6c980'}}}een': 1760285765, 'matching_hash': '98ae9ae4174799d3'}}}