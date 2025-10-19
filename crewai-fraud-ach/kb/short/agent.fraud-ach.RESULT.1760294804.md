```json
{
  "id": "49138213f23340b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294804,
  "host_pid": "9e6742732c60:1",
  "hash": "224af6f688f5001f459aa3b817fe2b7c1b029e9205a0c954be45856601b5bd4e",
  "cid": "QmV1224af6f688f5001f459aa3b817fe2b7c1b029e92",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294804,
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
      "evaluated_at": 1760294804
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
  "sig": "294904ea1fab1848fedb00212a4a77742f7add7c0605db64c06341971e4142ea"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590985666
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 49063455, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285763, 'matching_hash': 'a91912abaf20cb4f'}}}