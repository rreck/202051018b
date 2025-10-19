```json
{
  "id": "f754b2d742c98422",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287332,
  "host_pid": "9e6742732c60:1",
  "hash": "44d3bfef1a170c49524a56fafa1e5916fbee160dc491a9a729a9ac02f7ba341c",
  "cid": "QmV144d3bfef1a170c49524a56fafa1e5916fbee160d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287332,
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
      "evaluated_at": 1760287332
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "63e9db5836a3424313f59ba5777eebca292f7c35e015683a03de54e4e2bb139f"
}
```

Fraud detected: duplicate_transaction (score: 73)
Transaction: 031201463882943
Details: {'velocity': {'fraud_detected': True, 'risk_score': 62, 'details': {'transaction_count': 56, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 55, 'first_seen': 1760285765, 'matching_hash': '0eb18222520b1d39'}}}