```json
{
  "id": "5da0d0e8d995d83f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286123,
  "host_pid": "9e6742732c60:1",
  "hash": "846d5f0d453884beac1399d25fc69883f5bfdd87165184907b4f0aa8c3c569f7",
  "cid": "QmV1846d5f0d453884beac1399d25fc69883f5bfdd87",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286123,
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
      "evaluated_at": 1760286123
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
  "sig": "1b00c469758d86c026d2215c7d5a4fbfd69cb92b3abcb6146a309b2405a716ac"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000028666977
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 14, 'first_seen': 1760285763, 'matching_hash': '3b5947d2333162a8'}}}, 'risk_score': 85, 'details': {'duplicate_count': 14, 'first_seen': 1760285763, 'matching_hash': '10c7ec0cec0e62a6'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}