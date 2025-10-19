```json
{
  "id": "d9af86a4472af187",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287403,
  "host_pid": "9e6742732c60:1",
  "hash": "8187a7985215ac898ac993c114768fd876894be6c4682375d23547368f4d5e37",
  "cid": "QmV18187a7985215ac898ac993c114768fd876894be6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287403,
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
      "evaluated_at": 1760287403
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "cf7c61e3006335e0fe85daed9a2eaf438f5b16b0491702d1404000acfdb47105"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 864091464204372
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 59, 'threshold': 50, 'total_amount': 13960521, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 58, 'first_seen': 1760285763, 'matching_hash': '74f25dd839f89a8f'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '864091464', 'validation_error': 'Invalid routing number checksum'}}}