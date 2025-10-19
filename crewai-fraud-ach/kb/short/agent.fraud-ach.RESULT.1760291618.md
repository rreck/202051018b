```json
{
  "id": "119151aff69949ca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291618,
  "host_pid": "9e6742732c60:1",
  "hash": "465959bc3b5dd64be0024d3165ea330f6cb382e410f59312652b6b0d6bfa011a",
  "cid": "QmV1465959bc3b5dd64be0024d3165ea330f6cb382e4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291618,
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
      "evaluated_at": 1760291618
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
  "sig": "831ec11473308c89261a3a263099a1c854c6636d5cc90247a2ecfe4ccd8f29bc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021173532
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 55180151, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285763, 'matching_hash': 'a0cc7134a86fdd26'}}}