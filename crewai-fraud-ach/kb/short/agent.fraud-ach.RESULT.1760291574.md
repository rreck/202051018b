```json
{
  "id": "23e93fe84c27ba47",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291574,
  "host_pid": "9e6742732c60:1",
  "hash": "2717c76e54ff969ee45a052120e9c79f2e1ba65d99e89931c5ec500f2f134386",
  "cid": "QmV12717c76e54ff969ee45a052120e9c79f2e1ba65d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291574,
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
      "evaluated_at": 1760291574
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
  "sig": "2ef9c49ea0ba474ea5f763db6394382f260a1625ff85fac6de9f469b8b2ce168"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037120396
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 20118450, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285763, 'matching_hash': '29cd45017b863efa'}}}