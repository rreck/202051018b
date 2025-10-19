```json
{
  "id": "74e0adbb0d0919c3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286497,
  "host_pid": "9e6742732c60:1",
  "hash": "7a37cf11c015e4aed783d7b4443081574c3fe5ba32f85e77f171218b94c15312",
  "cid": "QmV17a37cf11c015e4aed783d7b4443081574c3fe5ba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286497,
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
      "evaluated_at": 1760286497
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
  "sig": "0941165c45145f1a0bede3e214547399bbd96c91f3f8880806bcde92020c875a"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000021005824
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 26, 'first_seen': 1760285763, 'matching_hash': '58a86144ce85b895'}}}