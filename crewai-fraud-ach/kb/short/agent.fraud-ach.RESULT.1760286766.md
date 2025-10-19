```json
{
  "id": "c4fb608faccc54ce",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286766,
  "host_pid": "9e6742732c60:1",
  "hash": "caa4622a79fe11727ac0b8cd6f9e3a2f9ada9fecde45983f881268c5b399a426",
  "cid": "QmV1caa4622a79fe11727ac0b8cd6f9e3a2f9ada9fec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286766,
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
      "evaluated_at": 1760286766
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
  "sig": "065ed8ab05556a3253a588a567908bba9aaa13c438edd2044cb57e17e7d326ee"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009598206386
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11180124, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 35, 'first_seen': 1760285765, 'matching_hash': '83614fe1c845b0af'}}}