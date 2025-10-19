```json
{
  "id": "579c244da38b861e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291220,
  "host_pid": "9e6742732c60:1",
  "hash": "07e8bf087ae8d31da278f1cabbac1c4c31d1f0c9a9140929bb8e48985db7d5bc",
  "cid": "QmV107e8bf087ae8d31da278f1cabbac1c4c31d1f0c9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291220,
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
      "evaluated_at": 1760291220
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
  "sig": "747c6f7739c638e72943f83ed0551e75ac730727b9c2898d639a7e3b5fd877ab"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030152104
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 49454190, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285763, 'matching_hash': 'f9baa0480a932ad2'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '530764331', 'validation_error': 'Invalid routing number checksum'}}}