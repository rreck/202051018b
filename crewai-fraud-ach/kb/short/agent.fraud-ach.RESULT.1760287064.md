```json
{
  "id": "0d474e0f416ad306",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287064,
  "host_pid": "9e6742732c60:1",
  "hash": "b55792be570adb047177389c655b4dd06b06ae1ddcd17243b74f38a38d6ff47e",
  "cid": "QmV1b55792be570adb047177389c655b4dd06b06ae1d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287064,
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
      "evaluated_at": 1760287064
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
  "sig": "184f6e28456a47076361605de73fb1ad7447538f4b2574f379d55e800af1d689"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100271879965
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 46, 'first_seen': 1760285763, 'matching_hash': '9c4837aa9a8e4a4a'}}}